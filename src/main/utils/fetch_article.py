from functools import wraps
from src.main.models.article import Article
from inspect import getattr_static


def fetch_article(f, **fields):
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['article'] = fields['article']

        return f(*args, **kwargs)

    return wrapper


def fetch_article_all_methods(Cls):
    class NewCls(object):

        def __init__(self, *args, **kwargs):
            if kwargs['article']:
                self.article = kwargs['article']
            else:
                url = kwargs['url']
                self.article = Article.objects.filter(url=url).first()

            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if isinstance(getattr_static(Cls, s), staticmethod):
                return fetch_article(x, article=self.article)
            else:
                return x

    return NewCls

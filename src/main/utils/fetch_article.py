from functools import wraps
from src.main.models.article import Article


def fetch_article(f, **fields):
    @wraps(f)
    def wrapper(*args, **kwargs):
        url = fields['url']
        article = Article.objects.filter(url=url).first()
        if not article:
            raise Exception('Invalid article url.')

        kwargs['article'] = article
        return f(*args, **kwargs)

    return wrapper


def fetch_article_all_methods(Cls):
    class NewCls(object):

        def __init__(self, *args, **kwargs):
            self.url = kwargs['url']
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__):  # it is an instance method
                return fetch_article(x, url=self.url)
            else:
                return x

    return NewCls

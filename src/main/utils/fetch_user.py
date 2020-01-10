from functools import wraps
from src.main.models.user import User
from inspect import getattr_static


def fetch_user(f, **fields):
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['user'] = fields['user']

        return f(*args, **kwargs)

    return wrapper


def fetch_user_all_methods(Cls):
    class NewCls(object):

        def __init__(self, *args, **kwargs):
            self.user = User.objects.filter(email=kwargs['email']).first()
            if not self.user:
                raise Exception('Invalid email or password.')
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
                return fetch_user(x, user=self.user)
            else:
                return x

    return NewCls

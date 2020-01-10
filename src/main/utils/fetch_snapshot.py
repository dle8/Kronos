from functools import wraps
from src.main.models.snapshot import Snapshot
from inspect import getattr_static

from flask import session


def fetch_snapshot(f, **fields):
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['snapshot'] = fields['snapshot']

        return f(*args, **kwargs)

    return wrapper


def fetch_snapshot_all_methods(Cls):
    class NewCls(object):

        def __init__(self, *args, **kwargs):
            self.snapshot = Snapshot.objects.filter(email=session['email']).filter(name=kwargs['name']).first()
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
                return fetch_snapshot(x, snapshot=self.snapshot)
            else:
                return x

    return NewCls

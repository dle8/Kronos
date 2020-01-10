from functools import wraps
from src.main.models.snapshot import Snapshot

from flask import session


def fetch_snapshot(f, **fields):
    @wraps(f)
    def wrapper(*args, **kwargs):
        email = session['email']
        snapshots = Snapshot.objects.filter(email=email)
        if fields.get('name', None):
            snapshots = snapshots.filter(name=fields['name']).first()

        kwargs['snapshot'] = snapshots
        return f(*args, **kwargs)

    return wrapper


def fetch_snapshot_all_methods(Cls):
    class NewCls(object):

        def __init__(self, *args, **kwargs):
            self.email = kwargs['email']
            self.name = kwargs['name']
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
                return fetch_snapshot(x, email=self.email, name=self.name)
            else:
                return x

    return NewCls

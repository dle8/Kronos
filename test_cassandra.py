from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import json
from graphene import ObjectType, String, Schema, Field, List, NonNull
from datetime import datetime
from inspect import getattr_static

# import yfinance as yf
#
# msft = yf.Ticker('MSFT')
# # print(msft.info)
# s = yf.download('MSFT', start='2000-01-01', end='2017-04-30')
# print(len(s))

#
# cluster = Cluster()
# session = cluster.connect('test')
#
# connection.setup(['127.0.0.1'], 'test', protocol_version=3)
#
#
# class Automobile(Model):
#     manu = columns.Text(primary_key=True)
#     year = columns.Integer(primary_key=True)
#     model = columns.Text()
#     price = columns.Decimal()
#     options = columns.Set(columns.Text)
#     created = columns.Date(datetime.now().date())
#
#
# sync_table(Automobile)
# Automobile.create(manu='Tesla', year=2020, model='Model 3', price=50000, options={'windows'}, created=datetime.now().date())
# q = Automobile.objects.filter(manu='Tesla').first()
# print(str(q.created))
# for op in q.options:
#     print(op.created)
# print(q.options)

# print(q.price)

# class Query(ObjectType):
#     hello = String(name=String(default_value='stranger'))
#     goodbye = String()
#
#     def resolve_hello(self, info, name):
#         return 'Hello, {}'.format(name)
#
#     def resolve_goodbye(self, info):
#         return 'good bye'
#
#
# # schema = Schema(query=Query)
# # query_string = '{ hello(name: "graphql") }'
# # result = schema.execute(query_string)
# # print(result.data['hello'])
#
# class Person(ObjectType):
#     first_name = String()
#     last_name = String()
#     full_name = String()
#     babies = List(String)
#
#     def resolve_full_name(parent, info):
#         return '{} {}'.format(parent.first_name, parent.last_name)
#
#     @staticmethod
#     def resolve_babies(parent, info):
#         return ['a', 'b']
#
#
# class Container(ObjectType):
#     email = String(required=True)
#     pp = Field(Person)
#
#     @staticmethod
#     def resolve_email(parent, info, **kwargs):
#         return parent.email
#
#     @staticmethod
#     def resolve_pp(parent, info, **kwargs):
#         return Person(first_name="Luke", last_name="S")
#
#
# class Query(ObjectType):
#     # me = Field(Container)
#     me = List(NonNull(Container), email=String())
#
#     def resolve_me(parent, info, **kwargs):
#         if kwargs.get('email', None):
#             return [Container(email=kwargs['email'])]
#         return [Container(email=email) for email in ['123@gmail.com', '456@gmail.com']]
#
#
# schema = Schema(query=Query)
# query_string = '''
#     {
#         me(email: "haha@gmail.com") {
#             email
#             pp {
#                 fullName,
#                 babies
#             }
#         }
#     }
# '''
# result = schema.execute(query_string)
# print(json.dumps(result.data, indent=2))
# # print(result.data)


def time_this(original_function, **additional_fields):
    print("decorating")

    def new_function(*args, **kwargs):
        print("starting timer")
        import datetime
        before = datetime.datetime.now()
        for k, v in additional_fields['info'].items():
            kwargs[k] = v
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after - before))
        return x

    return new_function


def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)
            self.data = kwargs['data']

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
            # print(type(self.oInstance))
            if isinstance(getattr_static(Cls, s), staticmethod):
                return time_this(x, info={'email': self.data})
            else:
                return x

    return NewCls


# now lets make a dummy class to test it out on:

@time_all_class_methods
class Foo(object):

    def __init__(self, *args, **kwargs):
        pass

    def a(self, **kwargs):
        print("entering a")
        print(kwargs['email'])
        import time
        time.sleep(3)
        print("exiting a")

    @staticmethod
    def b(**kwargs):
        print("entering b")
        print(kwargs['email'])
        import time
        time.sleep(3)
        print("exiting b")


oF = Foo(data='a@gmail.com')
# oF.a()
oF.b()
#
# from flask import Flask, g
#
# app = Flask(__name__, template_folder='../../templates')
# with app.app_context():
#     print(g.get('foo'))

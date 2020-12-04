import os

class Config(object):
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI ='sqlite:///'+ os.path.join(os.path.abspath(os.path.dirname(__file__)), 'employees.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
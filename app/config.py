import os
#default config

class BaseConfig(object):
      DEBUG = True,
      SECRET_KEY= '\x99R^9\xa6\x0e\xc5\xa5\xc0\xe4\xa0BIB\xcf\xd9@Y\x8c\xad\x10:tT',
      SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'

#class DevelopmentConfig(BaseConfig):
#	  DEBUG=False
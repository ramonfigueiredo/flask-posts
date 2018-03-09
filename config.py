import os

# default config
class BaseConfig(object):
	DEBUG = False

	# A secret key should be as random as possible.
	# Your operating system has ways to generate pretty random stuff based on a
	# cryptographic random generator which can be used to get such a key:
	# >>> import os
	# >>> os.urandom(24)
	# Just take that thing and copy/paste into your code and your're done.
	SECRET_KEY = 'Sa\xe6\xadb\xf2\xb7\xbc\xbd\xbbEb\tNJ>\xe8\x87\xaf\xf3 \xdfq\x8c'

	## Example to set environment variable in linux (ubuntu)
	# > export DATABASE_URL="sqlite:///posts.db"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False
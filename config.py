import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'osmvoting.db')
# DATABASE_URI = 'postgresql://localhost/osmvoting'

NOMINATIONS = ['core', 'innovation', 'writing', 'mapping', 'community', 'ulf']
STAGE = 'call'
ADMINS = set([290271])  # Zverik

# Override these (and anything else) in config_local.py
OAUTH_KEY = ''
OAUTH_SECRET = ''
SECRET_KEY = 'sdkjfhsfljhsadf'

try:
    from config_local import *
except ImportError:
    pass

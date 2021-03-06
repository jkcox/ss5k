import os
basedir = os.path.abspath(os.path.dirname(__file__))
logdir = os.path.join(basedir, 'log')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_SCRF_ENABLED = True
SECRET_KEY = "%Sy@i$6$suq@0cNO"

# Mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = 'scrapscanner5000@garage-laptop.localdomain'
MAIL_MAX_EMAILS = None
MAIL_ASCII_ATTACHMENTS = False

# Administrator list
ADMINS = ['tyler@garage-laptop.localdomain']

# Scan Settings
SCAN_DELAY = 5

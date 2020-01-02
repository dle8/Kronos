class Config(object):
    DEBUG = True

    # Google mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''  # google app token
    MAIL_DEFAULT_SENDER = ''
    MAIL_APP_PASSWORDS = ''

    SECRET_KEY = 'secret'


config = Config()

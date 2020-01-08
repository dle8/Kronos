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

    # CASSANDRA
    KEYSPACE = 'kronos'
    REPLICATION_FACTOR = 3
    STRATEGY = 'SimpleStrategy'

    # NEVERBOUNCE
    EMAIL_VERIFICATION_URL = 'https://api.neverbounce.com/v4/single/check?key={}&email={}'
    NEVERBOUNCE_API_KEY = ''

    # ALPHA ADVANTAGE
    ALPHA_ADVANTAGE_API_KEY = ''
    ALPHA_ADVANTAGE_TIME_SERIES_INTRADAY_API = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}&outputsize={}&apikey={}'

    SECRET_KEY = 'secret'


config = Config()

from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 828161590  # my telegram ID
    OWNER_USERNAME = "cyberkiller7"  # my telegram username
    API_KEY = "1486553989:AAHToXlBrbOp1UmTmYGGNLki02OOYxo9Vpk"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://vsujpwwiuytmwb:ee078dc918b71c471e5e8c9d63805525496b8934e3ce0af4ff889f8694fd4eab@ec2-35-168-77-215.compute-1.amazonaws.com:5432/d3rg51is3l0v4p'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']

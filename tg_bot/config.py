from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 828161590  # my telegram ID
    OWNER_USERNAME = "cyberkiller7"  # my telegram username
    API_KEY = "1486553989:AAHToXlBrbOp1UmTmYGGNLki02OOYxo9Vpk"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://wkvqrqmotjtzuw:da3c0dfcff13ccde92494b8b0bb99531da78ea291bf8e2f17c1ea93fa458608c@ec2-54-205-26-79.compute-1.amazonaws.com:5432/ddiuicu89jg540'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']

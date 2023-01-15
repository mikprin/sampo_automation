# File with code for the telegram bot


# Importing libraries
import logging, dotenv, os, sys
import telebot
import redis
# Local imports
import msgs
from user import get_user_info
# Logging

import logging.handlers
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


# Importing settings and environment variables

script_dir_full = os.path.dirname(os.path.realpath(__file__))

try:
    dotenv.load_dotenv(os.path.join(script_dir_full, ".." ,'.env'))
    logging.info("Loaded .env file")
except Exception as e:
    logging.error("Error loading .env file: ", e)
    sys.exit(1)

# Initializing redis

redis_hosts = os.getenv("REDIS_HOSTS").split(",")
redis_port = os.getenv("REDIS_PORT")

for host in redis_hosts:
    connection = redis.Redis(
    host=host,
    port=redis_port,
    # port=6379,
    )
    try:
        if connection.ping():
            logging.info(f"Connected to redis host {host}")
            connected_to_redis = True
            redis_connection = connection
            break
    except Exception as e:
        logging.error(f"Could not connect to redis host {host}: {e}")
        # connected_to_redis = False
if not connected_to_redis:
    logging.error("Could not connect to redis")
    sys.exit(1)

redis_connection.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

print(redis_connection.get("Bahamas"))

# Telegram bot
telegram_token = os.getenv("TELEGRAM_API_KEY")

bot = telebot.TeleBot(telegram_token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN



# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     user_info = get_user_info(message)
#     logging.info(f"User with nickname {user_info['user_username']} started the bot.")
#     bot.reply_to(message, msgs.welcome_msg)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     user_input = message.text
#     user_info = get_user_info(message)
#     logging.info(f"User with nickname {user_info['user_username']} sent the message: {user_input}")
#     bot.reply_to(message, "received your message")
    
# bot.infinity_polling()
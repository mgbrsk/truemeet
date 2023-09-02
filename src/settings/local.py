from os import getenv

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

TG_BOT_TOKEN = getenv('TG_BOT_TOKEN')

# import asyncio


# async def main() -> None:
#     print('run main')


# asyncio.run(main())

import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()  # take environment variables from .env.
engine = create_engine("sqlite+pysqlite:///european_database.sqlite")

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("TG_BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
user_list = set()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    logging.info(message.from_user.username)
    user_list.add(message.from_user.username)
    if len(user_list) == 1:
        greet_username = f"You and only you, {message.from_user.username}, little bastard :3"
    else:
        greet_username = f"{message.from_user.username} (yea, thats you, little bastard :3)"
    # message.username
    await message.answer(f"Hey, {hbold(message.from_user.full_name)}! "
                         f"Another users:\n {', '.join(str(item) for item in user_list).replace(message.from_user.username, greet_username)}")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

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
import sqlalchemy as sa
from sqlalchemy import create_engine
from src.db import User
load_dotenv()  # take environment variables from .env.
# engine = create_engine("sqlite+pysqlite:///truemeet.sqlite")
engine = create_engine(f"postgresql+psycopg2://{getenv('BD_USER')}:{getenv('BD_PASSWORD')}@localhost:5433/postgres")

connection = engine.connect()
# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("TG_BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

output_user = connection.execute(sa.select(User.username)).fetchall()
output_user_id = connection.execute(sa.select(User.user_id)).fetchall()

user_list = [x[0] for x in output_user]
user_id_list = [x[0] for x in output_user_id]
print(user_list, user_id_list)


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
    current_username = message.from_user.username
    current_user_id = str(message.from_user.id)
    logging.info(f'{current_username}, {current_user_id}')
    
    if current_user_id not in user_id_list:
        logging.info(f'{current_user_id} not in {user_id_list}')
        user_list.append(current_username)
        user_id_list.append(current_user_id)
        
        query = sa.insert(User).values(username=current_username, user_id=message.from_user.id)
        connection.execute((query))
        connection.commit()
    else:
        logging.info(f'Found user {user_id_list} in {current_user_id}.')
    
    if len(user_list) == 1:
        greet_username = f"You and only you, {current_username}, little bastard :3"
    else:
        greet_username = f"{current_username} (yea, thats you, little bastard :3)"
    # message.username
    await message.answer(f"Hey, {hbold(message.from_user.full_name)}! "
                         f"Another users:\n {', '.join(str(item) for item in user_list).replace(current_username, greet_username)}")


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

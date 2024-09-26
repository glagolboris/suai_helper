from onboard_bot import OnboardBot
import asyncio
import os
from dotenv import load_dotenv
import logging
from gigachat_requests.set_data import set_data


if __name__ == '__main__':
    logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)
    load_dotenv('.env')
    bot = OnboardBot(os.environ.get('BOT_API'))
    asyncio.run(bot.run_async_functions())
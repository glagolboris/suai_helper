from aiogram import Bot, Dispatcher
from gigachat_requests.auth import OAuth
import os
from dotenv import load_dotenv
from database import Database
from handlers.state_handlers import state_handlers
from handlers.text_handlers import text_handlers
from handlers.command_handlers import command_handlers
from handlers.callback_handlers import callback_handlers
from get_data_from_docx import Reconstructor
from parsers.parser_of_teachers_guap import ParserProfessors
from middlewars.register_middlewares import register_mw
import aiohttp
from gigachat_requests.embedding_model import EmbeddingModel
from gigachat_requests.set_data import set_data

# ToDo:
#   1. Сделать хендлеры ошибок:
#       1. none auth data (gigachat)
#   2. Сделать историю сообщений пользователя (json)
#   знаменатель - нечетный, числитель - четный
#   день//14 % 2


class OnboardBot:
    def __init__(self, token):
        load_dotenv('.env')
        self.bot = Bot(token)
        self.dispatcher = Dispatcher()

        db = Database()
        self.connection, self.cursor = db.run_bd()

        set_data('data/test.txt', self)

        gigachat_model = OAuth(os.environ["AUTH_DATA"])
        self.gigachat = gigachat_model.oauth()

        emb_model = EmbeddingModel(os.environ["AUTH_DATA"])
        self.database_qa = emb_model.db

        reconstructor = Reconstructor('Расписание всех групп с 09.02.2024.docx')
        reconstructor.send_data_to_db(self_bot=self)

        self.run_sync_functions()

    def run_sync_functions(self):
        state_handlers(self)
        text_handlers(self)
        command_handlers(self)
        callback_handlers(self)

    async def run_async_functions(self):
        register_mw(self)
        # await self.send_professors_to_bd()
        await self.dispatcher.start_polling(self.bot)

    async def send_professors_to_bd(self):
        async with aiohttp.ClientSession() as session:
            parser = ParserProfessors(session, self_bot=self)
            await parser.send_data_to_bd()


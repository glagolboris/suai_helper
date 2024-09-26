import re
from states import Form
from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from buttons.profile_markup import get_profile_markup


class Middleware(BaseMiddleware):
    def __init__(self, self_bot):
        self.self_bot = self_bot

    async def __call__(self, *args, **kwargs):
        pass


class MiddlewareExitFromTheGroup(Middleware):
    async def __call__(self, handler, event, data):
        if Form.group and re.search('Выйти из раздела', event.text):
            await self.self_bot.bot.send_message(event.chat.id, '✍🏼 Вы можете указать свою группу позже, но пока вам не доступны следующие возможности 📝:\n1. Рассылка изменений\nНо вы все также можете использовать модель Gigachat для получения нужной вам информации в рамках университета.', reply_markup=get_profile_markup())
            state: FSMContext = data.get('state')
            await state.clear()

            self.self_bot.cursor.executemany("""INSERT INTO students VALUES(%s, %s, %s)""", [(None, event.chat.id, None)])
            self.self_bot.connection.commit()
        else:
            return await handler(event, data)


class MiddlewareExitFromTheChangeGroup(Middleware):
    async def __call__(self, handler, event, data):
        if Form.chane_group and re.search('Выйти из раздела', event.text):
            await self.self_bot.bot.send_message(event.chat.id, '⏪︎ Вы вышли из раздела', reply_markup=get_profile_markup())

            state: FSMContext = data.get('state')
            await state.clear()

        else:
            return await handler(event, data)


class MiddlewareExitFromTheDialog(Middleware):
    async def __call__(self, handler, event, data):
        if Form.dialog and re.search('Выйти из раздела', event.text):
            await self.self_bot.bot.send_message(event.chat.id, '⏪︎ Вы вышли из раздела', reply_markup=get_profile_markup())
            state: FSMContext = data.get('state')
            await state.clear()

        else:
            return await handler(event, data)
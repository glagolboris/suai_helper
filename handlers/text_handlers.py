import re
from aiogram.types import Message
from buttons.change_group_markup import get_change_group_markup
from buttons.exit_from_the_chapter_markup import exit_from_the_chapter
from aiogram.fsm.context import FSMContext
from states import Form


def text_handlers(self):
    @self.dispatcher.message(lambda message: re.search('Мой профиль', message.text))
    async def get_profile(message: Message):
        self.cursor.execute(f"""SELECT group_name, id FROM students WHERE id = {message.chat.id}""")
        data = self.cursor.fetchall()[0]
        await self.bot.send_message(message.chat.id, f'🆔 {data[1]}\n👥 Группа {"Не определена" if data[0] is None else data[0]}', reply_markup=get_change_group_markup())

    @self.dispatcher.message(lambda message: re.search('Спросить', message.text))
    async def ask_model(message: Message, state: FSMContext):
        await self.bot.send_message(message.chat.id, 'Введите вопрос gigachat модели.', reply_markup=exit_from_the_chapter())
        await state.set_state(Form.dialog)

    @self.dispatcher.message(lambda message: re.search('Выйти из раздела', message.text))
    async def exit_from_the_chapter_func(message: Message):
        await self.bot.send_message(message.chat.id, '⏪︎ Вы вышли из раздела.', reply_markup=get_change_group_markup())




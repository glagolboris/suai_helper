from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Form
from buttons.exit_from_the_chapter_markup import exit_from_the_chapter


def command_handlers(self):
    @self.dispatcher.message(Command('start'))
    async def start_handler(message: Message, state: FSMContext):
        await self.bot.send_message(message.chat.id, "👋 Здравствуйте, это Хелпер - ваш 🤖 бот-помощник для обучения/работы в ГУАП'е. С ним вы можете узнать актуальное 🗓 расписание, а также его изменение. узнать ФИО 🧑‍🏫 преподавателя и многое другое.")
        await self.bot.send_message(message.chat.id, "✍🏼 Но для начала напишите группу, в которой вы учитель без 'C'.", reply_markup=exit_from_the_chapter())
        await state.set_state(Form.group)

from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states import Form
from buttons.exit_from_the_chapter_markup import exit_from_the_chapter


def callback_handlers(self):
    @self.dispatcher.callback_query(lambda cq: cq.data == 'change_group')
    async def change_group(cq: CallbackQuery, state: FSMContext):
        await self.bot.send_message(cq.message.chat.id, '✍🏼 Введите новую группу без "С".', reply_markup=exit_from_the_chapter())
        await state.set_state(Form.chane_group)
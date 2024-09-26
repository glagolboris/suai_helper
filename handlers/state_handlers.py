from states import Form
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from buttons.profile_markup import get_profile_markup
from langchain.chains import RetrievalQA


def state_handlers(self):
    @self.dispatcher.message(Form.group)
    async def get_group_state(message: Message, state: FSMContext):
        self.cursor.execute("""SELECT group_name FROM timetable""")
        groups = [group[0] for group in self.cursor.fetchall()]
        if 'С'+message.text in groups:
            self.cursor.executemany("""INSERT INTO students VALUES(%s, %s, %s)""", [('С'+message.text, message.chat.id, None)])
            self.connection.commit()
            await self.bot.send_message(message.chat.id, '✅️ Вы успешно зарегистрировались в боте.', reply_markup=get_profile_markup())
            await state.clear()
        else:
            await self.bot.send_message(message.chat.id, '❌ Группа не найдена. Вы можете добавить группу позже.')

    @self.dispatcher.message(Form.chane_group)
    async def change_group(message: Message, state: FSMContext):
        self.cursor.execute("""SELECT group_name FROM timetable""")
        groups = [group[0] for group in self.cursor.fetchall()]
        if 'С'+message.text in groups:
            self.cursor.execute(f"""UPDATE students SET group_name = '{'С'+message.text}' WHERE id = {message.chat.id}""")
            self.connection.commit()
            await state.clear()
            await self.bot.send_message(message.chat.id, '✅️ Вы успешно изменили группу в боте.', reply_markup=get_profile_markup())
        else:
            await self.bot.send_message(message.chat.id, '❌ Группа не найдена. Введите еще раз или выйдете из раздела.')

    @self.dispatcher.message(Form.dialog)
    async def ask_model(message: Message):
        qa_model = RetrievalQA.from_chain_type(self.gigachat, retriever=self.database_qa.as_retriever())
        res = qa_model({'query': message.text})

        await self.bot.send_message(message.chat.id, res['result'])


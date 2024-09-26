from langchain.schema import HumanMessage, SystemMessage
from onboard_bot import OnboardBot
from aiogram.types import Message


class PostmanToGigachat:
    def __init__(self, self_bot: OnboardBot, message: Message):
        self.self_bot = self_bot
        self.message = message

    def send_message(self):
        self.self_bot.cursor.execute(f"""SELECT history FROM students WHERE id = {self.message.chat.id}""")
        data = self.self_bot.cursor.fetchall()[0]




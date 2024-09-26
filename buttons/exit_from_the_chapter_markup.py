from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup


def exit_from_the_chapter() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    exit_button = KeyboardButton(text='⏪︎ Выйти из раздела')
    builder.row(exit_button)

    return builder.as_markup(resize_keyboard=True)

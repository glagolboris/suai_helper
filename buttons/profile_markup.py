from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder, ReplyKeyboardMarkup


def get_profile_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    profile = KeyboardButton(text='🇮 Мой профиль')
    start_dialog = KeyboardButton(text='🔍️ Спросить')

    builder.row(profile)
    builder.row(start_dialog)

    return builder.as_markup(resize_keyboard=True)
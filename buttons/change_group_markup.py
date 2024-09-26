from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


def get_change_group_markup():
    builder = InlineKeyboardBuilder()
    change_button = InlineKeyboardButton(text='Изменить группу', callback_data='change_group')
    builder.row(change_button)

    return builder.as_markup()
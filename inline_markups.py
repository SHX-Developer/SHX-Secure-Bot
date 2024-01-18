from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



#  INLINE
inline = InlineKeyboardMarkup()
inline.row(InlineKeyboardButton(text = "button_1", callback_data = "button_1"))
inline.row(InlineKeyboardButton(text = "button_2", callback_data = "button_2"))
inline.row(InlineKeyboardButton(text = "button_3", callback_data = "button_3"))
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import emoji

main_caption = emoji.emojize('Пойдем покурим 🚬🚬🚬')
button_smoke = KeyboardButton(f"/{main_caption}")

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_smoke)

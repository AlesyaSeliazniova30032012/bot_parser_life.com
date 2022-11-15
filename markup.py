from telebot import types

kb_shop = types.InlineKeyboardButton(text='Перейти в магазин', callback_data='shop')
kb_help = types.InlineKeyboardButton(text='Консультация специалиста', callback_data='help')
kb_smartphones = types.InlineKeyboardButton(text='Смартфоны', callback_data='smartphones')
kb_accessories = types.InlineKeyboardButton(text='Умные устройства', callback_data='accessories')
kb_modems = types.InlineKeyboardButton(text='Роутеры', callback_data='modems')


kb = types.InlineKeyboardMarkup()
kb.add(kb_shop, kb_help)

kb1 = types.InlineKeyboardMarkup()
kb1.add(kb_shop)

kb_shop = types.InlineKeyboardMarkup()
kb_shop.add(kb_smartphones, kb_accessories, kb_modems)

kb_smartphones = types.InlineKeyboardMarkup()
kb_smartphones.add(kb_accessories, kb_modems)
kb_smartphones.add(kb_help)

kb_accessories = types.InlineKeyboardMarkup()
kb_accessories.add(kb_smartphones, kb_modems)
kb_accessories.add(kb_help)

kb_modems = types.InlineKeyboardMarkup()
kb_modems.add(kb_smartphones, kb_accessories)
kb_modems.add(kb_help)


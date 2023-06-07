from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove

kb1=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
b1=KeyboardButton(text="/Royxatga_olish")

kb1.add(b1)

# yo'nalishni tanlash uchun inline buttonlar
ikb1=InlineKeyboardMarkup(row_width=2)
ib1=InlineKeyboardButton(text="Kompyuter savodxonligi",
                         callback_data='KS')
ib2=InlineKeyboardButton(text="Python Dasturlash",
                         callback_data="pyd")
ikb1.add(ib1).add(ib2)

kb2=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(text='Raqamni yuborish', request_contact=True))
remuv=ReplyKeyboardRemove()

# ___________________________________Admin uchun tugmalar__________________________________________

akb1=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
ab1=KeyboardButton(text="db_malumot")
ab2=KeyboardButton(text="db_clear")

akb1.add(ab1).add(ab2)

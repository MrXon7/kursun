from aiogram import types,Bot,Dispatcher,executor
from aiogram.dispatcher.filters import Text  # filterdan Text classini chaqirish
import pandas as pd
from btns import kb1,ikb1,kb2,remuv,akb1
from database import add_id,conn,malumot_olish,add_fish,add_num,add_yonalish,db_clear,ids

try:
    import requests
    Token_API='6265160696:AAGL-TEJfAoYE1cunQ3uRjUQeR4J_AiMWSA'
    
    bot=Bot(Token_API)
    dp=Dispatcher(bot)

    start_text="""
    Assalomu aleykum. Hush kelibsiz.
    "Kompyuter savodxonligi" va
    "Boshlang'ich Pyhon dasturlash asoslari" kurslarimizga ro'yxatda o'tish uchun pasdagi
    <b><em>/Royxatga_olish</em></b>  tugmasini bosing

    Bot haqida ma'lumot olish uchun /help buyrug'ini kiriting
    """
    help_text="""
    Bu bot yaqin kunlarda boshlanadigan "Kompyuter savodxonligi" va
    "Boshlang'ich Pyhon dasturlash asoslari" kurslarimizgan ro'yxatga olish uchun xizmat
    qiladi. Ro'yxatdan o'tish uchun <b><em>/Royxatga_olish</em></b>
    Buyrug'ini kiriting yoki pasdagi tugmani bosing 
    """

    @dp.message_handler(commands=['start'])
    async def start_comm(message: types.Message):
        try:
            userid=message.from_user.id
            if userid != 6233455730:
                await message.answer(text=start_text,
                                parse_mode='HTML',
                                reply_markup=kb1)
                await message.delete()
            else:
                await message.answer(text="Xush kelibsiz boss",reply_markup=akb1)
        except:
            await message.answer(text="texnik nosozlik. botni qaytadan ishlatib ko'ring")
    

    @dp.message_handler(commands=['help'])
    async def help_comm(message: types.Message):
        userid=message.from_user.id
        if userid != 6233455730:
            await bot.send_message(chat_id=message.from_user.id, text=help_text,
                            parse_mode='HTML')
        else:
            await message.answer(text="Buyruqlar \n<b><em>db_malumot</em></b> \n<b><em>db_clear</em></b> \n<b><em>excel</em></b>")

        
    async def on_startup(_):
        print("ishlayabdi")
        conn   
        global T
        T=0
        import requests
        github_pages_url = 'https://mrxon7.github.io/kursun/'

        webhook_url = f'https://api.telegram.org/bot{Token_API}/setWebhook?url={github_pages_url}'

        response = requests.get(webhook_url)
        if response.status_code == 200:
            print('Webhook URL has been set successfully.')
        else:
            print('Failed to set webhook URL.')

 # _________________________________________________________Adminlar uchun___________________________________________________

    @dp.message_handler(Text(equals='db_malumot'))
    async def set_excel(message: types.Message):
        userid=message.from_user.id
        count=1
        mal=malumot_olish()
        if userid==6233455730:
            if not mal:
                await bot.send_message(chat_id=userid, text="Ro'yxat toza")
            else:
                for A in mal:
                    await message.answer(text=f"{count}-foydalanuvchi\n{A}",parse_mode="HTML")
                    count+=1
        await message.delete()

    @dp.message_handler(Text(equals="db_clear"))
    async def set_excel(message: types.Message):
        userid=message.from_user.id
        if userid==6233455730:
            await db_clear()
            await message.answer(text="Baza tozalandi")
            await message.delete()

    
    # _______________________________________________Ro'yxatga olish________________________________________________

        

    @dp.message_handler(commands=['Royxatga_olish'])
    async def regs_comm(message: types.Message):
        # db ga userning id sini qo'shish
        userid=message.from_user.id
        await add_id(int(userid))
        
        
        await bot.send_message(chat_id=message.from_user.id, text="Ism va familiyangizni kiriting")
        await message.delete()
        global T
        T=1
        

    @dp.message_handler()
    async def get_fish(message:types.Message):
        global T 
        userid=message.from_user.id
        if T==1:
            # db ga xabarni fish sifatida qo'sh
            fish=message.text
            uid=message.from_user.id
            await add_fish(fish,uid)
            
            T=0
            await message.answer(text=f"{fish} siz qaysi yo'nalishda tahsil olmoqchisiz",
                                reply_markup=ikb1)
        # admin tomonidan foydalanuvchilarga xabar yozish
        elif userid==6233455730:
            txt=message.text
            photo=message.photo
            video=message.video
            caption=message.caption
            db_id=ids()
            for i in db_id:
                 # Xabarni foydalanuvchiga yuborish
                if txt:
                    await bot.send_message(chat_id=i, text=txt)
                elif photo:
                    await bot.send_photo(chat_id=i, photo=photo[-1].file_id, caption=caption)
                elif video:
                    await bot.send_video(chat_id=i, video=video.file_id, caption=caption)
                    
        # oddiy foydalanuvchi xabar yozsa qaytuchi javob  
        elif T==0:
            await message.answer(text="Noto'gri buyruq kiritildi. Qaytadan urinib ko'rin")
            
            

    @dp.callback_query_handler()
    async def cbd(callback: types.CallbackQuery):
        if callback.data =='KS':
            # db ga yo'nalishni ks sifatida qo'shish
            uid=callback.from_user.id
            await add_yonalish("ks",uid)
            
            await callback.answer(text="Kompyuter savodxonligi yo'nalishiga qo'shildingiz")
        elif callback.data == 'pyd':
            # db ga yo'nalishni pyd sifatida qo'shish
            uid=callback.from_user.id
            await add_yonalish("pyd",uid)
            
            await callback.answer(text="Python dasturlash kursiga qo'shildingiz ")

        await callback.message.answer("Iltimos telefon raqamingizni <em>Raqamni yuborish</em> tugmasi orqali yuboring",
                                    parse_mode="HTML",
                                    reply_markup=kb2)
        
        
    @dp.message_handler(content_types=types.ContentType.CONTACT)
    async def get_contact(message: types.Message):
        # db ga telefonraqamni qo'shish
        uid=message.from_user.id
        phone_num=message.contact.phone_number
        await add_num(phone_num,uid)
        
        await message.answer(text=f"Siz Muvaffaqiyat ro'yxatdan o'tdingiz. Guruh to'lishi bilan o'zimiz sizga aloqaga chiqamiz",
                            reply_markup=remuv)
    

   






    if __name__=='__main__':
        executor.start_polling(dispatcher=dp,
                            skip_updates=True,
                            on_startup=on_startup)
except:
    print("Xatolik")
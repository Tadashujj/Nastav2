import telebot
from telebot import types
bot=telebot.TeleBot("6697732049:AAF1_m6cV8wZ1-20h_bdOUJoUxSCCGE4MOo")
@bot.message_handler(commands=['curator'])
def chat(chat):
    
        use=types.InlineKeyboardMarkup()
        btn1=types.InlineKeyboardButton(text='Benjamin ⚡️', url='https://t.me/BenjaminDirector')
        btn2=types.InlineKeyboardButton(text='Qweef ⚡️',url='https://t.me/cabjah')
        btn3=types.InlineKeyboardButton(text='Соня Мармеладова ⚡️', url='https://t.me/president1881')
        use.add(btn1)
        use.add(btn2)
        use.add(btn3)
        bot.send_message(chat.chat.id,'Нехватает навыков СИ ? \n\
    выбирай себе наставника и вперед за работу !', reply_markup=use)
@bot.message_handler(commands=['tp'])
def chat(reg):
   tp=types.InlineKeyboardMarkup()  
   btn1=types.InlineKeyboardButton(text='Позвать тп❗', callback_data='tp')
   tp.add(btn1)
   bot.send_message(reg.chat.id,'Тп опять дрочат хуй знает где? Жми⬇️', reply_markup=tp)
@bot.callback_query_handler(func=lambda call: True)
def reg(reg):
   if reg.message:
       if reg.data=='tp':
           bot.edit_message_text(chat_id=reg.message.chat.id, message_id=reg.message.id, text='але хуисосы вы где????\n\
@BenjaminDirector, @president1881,@Prisedent777,@cabjah ')
   
bot.polling(none_stop=True)    
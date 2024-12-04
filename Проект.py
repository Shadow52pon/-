import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
import telebot
import time
from aiogram.types import ReplyKeyboardRemove 
ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)


logging.basicConfig(format='%(asctime)s -%(name)s -%(levelname)s -%(message)s', level=logging.DEBUG)

logger= logging.getLogger(__name__)

async def start(update,  context):
	user  =  update.effective_user
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = telebot.types.KeyboardButton('? Поздороваться')
	markup.add(btn1)
	await  update.message.reply_html(
	rf"Привет  {user.mention_html()}!  Я бот Электрон. Я помогу тебе узнать расписание уроков и консультаций!",)
	reply_markup=markup
	
async def help_command(update,  context):
	await update.message.reply_text('''Мои команды:
		1)Raspisanie7L
		2)Raspisanie7M
		3)Raspisanie7N
		4)Raspisanie8L
		5)Raspisanie8M
		6)Raspisanie8N
		7)Raspisanie9L
		8)Raspisanie9M
		9)Raspisanie9N
		10)Raspisanie10L
		11)Raspisanie10M
		12)Raspisanie10N
		13)Raspisanie11L
		14)Raspisanie11M
		15)Raspisanie11N
		16)Konsultacii(later)''')
		

async def Raspisanie7L(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test1.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie7N(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test3.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie8L(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test4.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)
				
async def Raspisanie7M(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test2.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie8M(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test5.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie8N(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test6.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie9L(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test7.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)	

async def Raspisanie9M(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test8.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)	

async def Raspisanie9N(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test9.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie10L(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test10.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie10M(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test11.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)	

async def Raspisanie10N(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test12.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie11L(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test13.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)	

async def Raspisanie11M(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test14.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)

async def Raspisanie11N(update,  context):
	with open('/storage/emulated/0/Music/Проект/Test15.jpg', 'rb') as photo:
				await update.message.reply_photo(photo)																																
					
async def phone(update,  context):
	await update.message.reply_text("Телефон:  +7(495)776-3030")
	
async def site(update,  context):
	await update.message.reply_text("Сайт:  https://www.yandex.ru/company")
	
async def work_time(update,  context):
	await update.message.reply_text("Время работы:  круглосуточно.")
	
application = Application.builder(). token("7845179531:AAGIzIyTlIA1i0Hh3NCjoO6aMEk6Lh0HDUQ").build()
application.add_handler(CommandHandler("start",  start))
application.add_handler(CommandHandler("help",  help_command))
application.add_handler(CommandHandler("Raspisanie7L", Raspisanie7L))
application.add_handler(CommandHandler("Raspisanie7M", Raspisanie7M))
application.add_handler(CommandHandler("Raspisanie7N", Raspisanie7N))	
application.add_handler(CommandHandler("Raspisanie8L", Raspisanie8L))
application.add_handler(CommandHandler("Raspisanie8M", Raspisanie8M))
application.add_handler(CommandHandler("Raspisanie8N", Raspisanie8N))
application.add_handler(CommandHandler("Raspisanie9L", Raspisanie9L))
application.add_handler(CommandHandler("Raspisanie9M", Raspisanie9M))
application.add_handler(CommandHandler("Raspisanie9N", Raspisanie9N))
application.add_handler(CommandHandler("Raspisanie10L", Raspisanie10L))
application.add_handler(CommandHandler("Raspisanie10M", Raspisanie10M))
application.add_handler(CommandHandler("Raspisanie10N", Raspisanie10N))
application.add_handler(CommandHandler("Raspisanie11L", Raspisanie11L))
application.add_handler(CommandHandler("Raspisanie11M", Raspisanie11M))
application.add_handler(CommandHandler("Raspisanie11N", Raspisanie11N))	
application.add_handler(CommandHandler("phone", phone))
application.add_handler(CommandHandler("site", site))
application.add_handler(CommandHandler("work_time", work_time))
application.add_handler(CommandHandler("help", help))
application.run_polling()


TOKEN = '<token_string>'
tb = telebot.TeleBot(TOKEN) #create a new Telegram Bot object

# TeleBot will not create thread for message listener. Default is True.
tb = telebot.TeleBot(TOKEN, False)

# 4 Thread worker for message listener.
tb = telebot.TeleBot(TOKEN, True, 4)

# Setup telebot handler to telebot logger. If you want to get some information from telebot.
# More information at Logging section
handler = logging.StreamHandler(sys.stdout)
telebot.logger.addHandler(handler)
telebot.logger.setLevel(logging.INFO)

# getMe
user = tb.get_me()

# sendMessage
tb.send_message(chatid, text)

# forwardMessage
# tb.forward_message(10894,926,3)
tb.forward_message(to_chat_id, from_chat_id, message_id)

# sendPhoto
photo = open('/tmp/photo.png', 'rb')
tb.send_photo(chat_id, photo)
file_id = 'AAAaaaZZZzzz'
tb.send_photo(chat_id, file_id)



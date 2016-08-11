import telegram  
from telegram.ext import Updater  
from telegram.ext import CommandHandler

Token = '249675148:AAEdP8CYLsqhAh2V8tDHWN4VVpnGdqycLBU'

mi_bot = telegram.Bot(token=Token)
mi_bot_updater = Updater(mi_bot.token)

def start(bot=mi_bot,update=mi_bot_updater):
    print ('Iniciando...')
    print (update.message.chat_id)
    bot.sendMessage(chat_id=update.message.chat_id, text="¿Que onda Campero?, preguntame tus dudas")
    
def ayuda(bot=mi_bot, update=mi_bot_updater):  
    print ('Solicita ayuda.')
    bot.sendMessage(chat_id=update.message.chat_id, text="No tengo mucho que ofrecerte por ahora")

def easterrandom(bot=mi_bot, update=mi_bot_updater):
    print ('Easter random.')
    bot.sendMessage(chat_id=update.message.chat_id, text="¡Aquí te va un easter aleatorio!, ve a la torre de agua del mapa mar rojo, ¡Avisame cuando estes ahí!")

def cualeaster(bot=mi_bot, update=mi_bot_updater):
    print('Pregunta que EE va a hacer')
    bot.sendMessage(chat_id=update.message.chat_id, text="¿Qué EE vas a realizar?")  

#Definimos para cada comando la función que atendera la peticion
start_handler = CommandHandler('start', start)  
ayuda_handler = CommandHandler('?', ayuda) 
easterrandom_handler = CommandHandler('easterrandom', easterrandom)

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)  
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(easterrandom_handler)

mi_bot_updater.start_polling()

while True:
    pass
    
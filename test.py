#Bot_wather_for_Telegram V2.0

import pyowm
import telebot

owm = pyowm.OWM('62d44e30046cb09806a689136f3cea17' , language="ru")

bot = telebot.TeleBot("825919917:AAEQxwn4LtrpFjuD0IdUB-Az5qRNTTgNirI") 

#стандартные команды бота
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	if message.text == "/start":
		welcome="Привет, я Бот-Погода! Для того, чтобы узнать погоду твоего города, введи его название! "

	elif message.text =="/help":
		welcome="Просто введи название своего города и я дам тебе свединия о погоде в данного города!"

	else:
		welcome="Я не знаю такую команду!"	

	bot.send_message(message.chat.id, welcome)

@bot.message_handler(content_types=['text'])

def send_echo(message):
	#список городов
	city=["Гродно","гродно","минск","Минск",
	"скидель","Скидель","дятлово","Дятлово","лида","Лида",
	"слоним","Слоним","мосты","Мосты","гомель","Гомель","Брест","брест",
	"барановичи","Барановичи","витебск","Витебск","Вороново","вороново","кореличи",
	"Кореличи","Щучин","щучин","Ивье","ивье"]

	#проверка города в списке городов
	if message.text in city:

		#поиск данных о погоде
		observation = owm.weather_at_place(message.text)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')["temp"]

		#вывод температуры (temp) и города (massage.text) 
		#стандартное сообщение бота
		answer="В городе " + message.text + " сейчас "+ w.get_detailed_status()+"\n" 
		answer+="Температура сейчас в районе " + str(temp) +"°С\n\n"

		#ответ бота сверянный с типом погоды
		if w.get_detailed_status()=="ясно":
			if temp<-10:
				answer+="На улицах города " + message.text + " мороз!"
			elif temp<0:
				answer+=" В такую погоду очень полезно будет прогуляться, но оденься потеплее))"
			elif temp<=15:
				answer+=" На улице уже тепловато, но в шортиках с майкой я бы еще не ходил)" 
			elif temp<=20:
				answer+=" Погода близится к жаркой, однако вечером нужно надеть куртку!"
			elif temp<=25:
				answer+=" Солнышко греет, погода супер, начинай набирать бассейн)) "
			elif temp>25:
				answer+=" Шикарная летняя температура воздуха, можно гулять до поздна не боясь простудиться!"

		elif w.get_detailed_status()=="пасмурно" or w.get_detailed_status()=="облачно" or w.get_detailed_status()=="слегка пасмурно":
			if temp<-10:
				answer+=" При такой погоде рекомендую лечь под пледик и залипнуть в любимый сериал)"
			elif temp<0:
				answer+=" Дойти до магазина и не замерзнуть вполне реально, только одевайся теплее!"
			elif temp<=15:
				answer+=" Обычная температура при такой погоде, если очень хочется то можно прогуляться" 
			elif temp<=20:
				answer+=" На улице тепло, если дождик не намечается то можно сходить с друзьями погулять"
			elif temp<=25:
				answer+=" Отличная погода для пикника!"
			elif temp>25:
				answer+=" Очень жарко, погода обманчива, возможен дождь!"

		elif w.get_detailed_status()=="дождь" or w.get_detailed_status()=="мелкий дождь" or w.get_detailed_status()=="гроза"  or w.get_detailed_status()=="легкий дождь":
			if temp<-10:
				answer+=" При такой погоде я бы из дому не выходил! "
			elif temp<0:
				answer+=" Отличное время погрустить, только не увлекайся)"
			elif temp<=15:
				answer+=" Отличное время погрустить, горячий чаек тебе в помощь, только не увлекайся) " 
			elif temp<=20:
				answer+=" Если ты на улице, то лучше переждать где-нибудь под навесом, т.к. при такой температуре дожди обычно не длятся долго)) "
			elif temp<=25:
				answer+=" Если ты на улице, то лучше переждать где-нибудь под навесом, т.к. при такой температуре дожди обычно не длятся долго))"
			elif temp>25:
				answer+=" Очень тепло, дождь только освежит тебя в такую погоду! "

		elif w.get_detailed_status()=="снег" or w.get_detailed_status()=="мокрый снег" or w.get_detailed_status()=="мелкий снег"  or w.get_detailed_status()=="легкий снег":
			if temp<-10:
				answer+=" Настоящая зима, время волшебства, но я бы пил горячий чай и смотрел фильмы)) "
			elif temp<0:
				answer+=" После баньки упасть в сугроб при такой температуре будет очень кстати!!"
			elif temp<=15:
				answer+=" Теплая зима, однако)" 
			elif temp<=20:
				answer+=" Вряд ли такое когда-либо случится, а если случилось, то жди слякоти на дорогах!"
	
	
	else:
		answer=" Я не знаю такого города:(\n\n Введите другой город :)"

	#вывод сообщения бота	
	bot.send_message(message.chat.id, answer)

bot.polling(none_stop= True)
import math
import telebot
from simpleeval import simple_eval

bot = telebot.TeleBot('BOT_TOKEN')

#command to get acquainted with a bot 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "description")

#help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "help instruction")

#command to call the list of commands
@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, "/start")
    bot.send_message(message.chat.id, "/help")
    bot.send_message(message.chat.id, "/commands")
    bot.send_message(message.chat.id, "/expression")
    bot.send_message(message.chat.id, "/sinRad")
    bot.send_message(message.chat.id, "/sinDeg")
    bot.send_message(message.chat.id, "/cosRad")
    bot.send_message(message.chat.id, "/cosDeg")
    bot.send_message(message.chat.id, "/tanRad")
    bot.send_message(message.chat.id, "/tanDeg")
    bot.send_message(message.chat.id, "/cotRad")
    bot.send_message(message.chat.id, "/cotDeg")
    bot.send_message(message.chat.id, "/secRad")
    bot.send_message(message.chat.id, "/secDeg")
    bot.send_message(message.chat.id, "/cosecRad")
    bot.send_message(message.chat.id, "/cosecDeg")
    bot.send_message(message.chat.id, "/arcsin")
    bot.send_message(message.chat.id, "/arccos")
    bot.send_message(message.chat.id, "/arctan")
    bot.send_message(message.chat.id, "/arccot")
    bot.send_message(message.chat.id, "/radianToDegreeConverter")
    bot.send_message(message.chat.id, "/degreeToRadianConverter")
 
#one line expression solving method
@bot.message_handler(commands=['expression'])
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry your expression (+ to add, - to subtract, / to divide, * to multiply, (), ** to exponentiate, % to modulus(remainder), ==, <, >, <=, >= to compare)")
    bot.register_next_step_handler(sent_expression, expression_solver)
def expression_solver(message):
    calc = message.text
    try:
        answer = simple_eval(calc)
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#basic trigonometric functions
#trigonometric function sin, where the entry data should be given in radians
@bot.message_handler(commands='sinRad')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in radians")
    bot.register_next_step_handler(sent_expression, sin)
def sin(message):
    try: 
        answer = str(format(math.sin(float(message.text)), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function sin, where the entry data should be given in degrees
@bot.message_handler(commands='sinDeg')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in degrees")
    bot.register_next_step_handler(sent_expression, sinDeg)
def sinDeg(message):
    try: 
        answer = str(format(math.sin(float(message.text) * math.pi / 180), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function cos, where the entry data should be given in radians
@bot.message_handler(commands='cosRad')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in radians")
    bot.register_next_step_handler(sent_expression, cos)
def cos(message):
    try: 
        answer = str(format(math.cos(float(message.text)), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function cos, where the entry data should be given in degrees
@bot.message_handler(commands='cosDeg')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in degrees")
    bot.register_next_step_handler(sent_expression, cosDeg)
def cosDeg(message):
    try: 
        answer = str(format(math.cos(float(message.text) * math.pi / 180), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)
    
#trigonometric function tan, where the entry data should be given in radians
@bot.message_handler(commands='tanRad')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in radians")
    bot.register_next_step_handler(sent_expression, tan)
def tan(message):
    try: 
        answer = str(format(math.tan(float(message.text)), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function tan, where the entry data should be given in degrees
@bot.message_handler(commands='tanDeg')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in degrees")
    bot.register_next_step_handler(sent_expression, tanDeg)
def tanDeg(message):
    try: 
        answer = str(format(math.tan(float(message.text) * math.pi / 180), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)
    
#trigonometric function cot, where the entry data should be given in radians
@bot.message_handler(commands='cotRad')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in radians")
    bot.register_next_step_handler(sent_expression, cot)
def cot(message):
    try: 
        answer = str(format(1 / math.tan(float(message.text)), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function cot, where the entry data should be given in degrees
@bot.message_handler(commands='cotDeg')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in degrees")
    bot.register_next_step_handler(sent_expression, cotDeg)
def cotDeg(message):
    try: 
        answer = str(format((1 / math.tan(float(message.text) * math.pi / 180)), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function sec, where the entry data should be given in radians
@bot.message_handler(commands='secRad')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in radians")
    bot.register_next_step_handler(sent_expression, sec)
def sec(message):
    try:
        answer = str(format((1 / math.cos(float(message.text))), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function sec, where the entry data should be given in degrees
@bot.message_handler(commands='secDeg')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in degrees")
    bot.register_next_step_handler(sent_expression, secDeg)
def secDeg(message):
    try:
        answer = str(format((1 / math.cos(float(message.text) * math.pi / 180)), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function cosec, where the entry data should be given in radians
@bot.message_handler(commands='cosecRad')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in radians")
    bot.register_next_step_handler(sent_expression, cosec)
def cosec(message):
    try:
        answer = str(format((1 / math.sin(float(message.text))), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function sec, where the entry data should be given in radians
@bot.message_handler(commands='cosecDeg')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in degrees")
    bot.register_next_step_handler(sent_expression, cosecDeg)
def cosecDeg(message):
    try:
        answer = str(format((1 / (math.sin((float(message.text) * math.pi / 180))))), '.10f')
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#inverse trigonometric functions   
#trigonometric function arcsin
@bot.message_handler(commands='arcsin')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value")
    bot.register_next_step_handler(sent_expression, arcsin)
def arcsin(message):
    try:
        answer = str(format(math.asin(float(message.text)), '.10f')) + "\n" + str(format((math.asin(float(message.text)) * 180 / math.pi), '.10f')) + "°"
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function arccos
@bot.message_handler(commands='arccos')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value")
    bot.register_next_step_handler(sent_expression, arccos)
def arccos(message):
    try:
        answer = str(format(math.acos(float(message.text)), '.10f')) + "\n" + str(format((math.acos(float(message.text))  * 180 / math.pi), '.10f')) + "°"
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function arctan
@bot.message_handler(commands='arctan')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value")
    bot.register_next_step_handler(sent_expression, arctan)
def arctan(message):
    try:
        answer = str(format(math.atan(float(message.text)), '.10f')) + "\n" + str(format((math.atan(float(message.text))  * 180 / math.pi), '.10f')) + "°"
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#trigonometric function arccot   
@bot.message_handler(commands='arccot')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value")
    bot.register_next_step_handler(sent_expression, arccot)
def arccot(message):
    try:
        answer = str(format(math.atan(1 / float(message.text)), '.10f')) + "\n" + str(format((math.atan(1 / float(message.text))  * 180 / math.pi), '.10f')) + "°"
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

#converters
#converter from radian to degree
@bot.message_handler(commands='radianToDegreeConverter')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in radians")
    bot.register_next_step_handler(sent_expression, RadToDegConverter)
def RadToDegConverter(message):
    try:
        answer = str(format((float(message.text) * 180 / math.pi), '.5f')) + "°"
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)
    
#converter from degree to radian
@bot.message_handler(commands='degreeToRadianConverter')
def receiver(message):
    sent_expression = bot.send_message(message.chat.id, "Entry the value in degrees")
    bot.register_next_step_handler(sent_expression, DegToRadConverter)
def DegToRadConverter(message):
    try:
        answer = str(format((float(message.text) * math.pi / 180), '.10f'))
    except Exception as e:
        answer = "Something went wrong, please write /help"
    bot.send_message(message.chat.id, answer)

bot.infinity_polling()

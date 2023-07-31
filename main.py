import telebot
Token = ""

bot = telebot.TeleBot(Token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum ramadon Vaqt botiga Hush Kelibsiz Shulardan Birini Tanlang /start  /vaqt  /python  /geo  /vidios  /yillik_vaqt  /Ramadon  /salovatlar /content  /contact  /java  /help .✨");


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
                 """
            /start -> Welcome to the channel.😇
            /help -> This praticular message.🥶
            /content -> About various Playlists of Simplilearn.🤝
            /python -> The frist vidio form Python playlist.🧠
            /SQL -> The frist vidio from SQl playlist.👀
            /java -> The frist vidio from java playlist.🎓
            /contact -> contact infarmation.🌸
                 """);
@bot.message_handler(commands=['contact'])
def cont(message):
    bot.reply_to(message, "https://youtu.be/1-QwkMkqgxE")

@bot.message_handler(commands=['content'])
def qayta(message):
    bot.reply_to(message, "https://youtu.be/f3G8LJptg9k")


@bot.message_handler(commands=['SQL'])
def sqll(message):
    bot.reply_to(message, "SqL vidio: https://youtu.be/AK7_m-aThfw")


@bot.message_handler(commands=['vaqt'])
def vaqt(message):
    bot.reply_to(message, "Ramadon: https://islom.uz/");


@bot.message_handler(commands=['python'])
def python(message):
    bot.reply_to(message, "Python: https://youtu.be/rfscVS0vtbw");


@bot.message_handler(commands=['geo'])
def geo(message):
    bot.reply_to(message, "Agar Yordam Kerak Bo'lsa @CEO_at_com ga murojat qiling 🌔");


@bot.message_handler(commands=['vidios'])
def vidios(message):
    bot.reply_to(message, "Vidios: https://youtu.be/gV3zNhbf37E");


@bot.message_handler(commands=['yillik_vaqt'])
def yillik_vaqt(message):
    bot.reply_to(message, "Vaqitlar: https://namozvaqti.uz/ramazon/toshkent")


@bot.message_handler(commands=["Ramadon"])
def ramadon_haqida(message):
    bot.reply_to(message, "Ramadon Haqida: https://youtu.be/kSJE-gY24Mc")
    bot.reply_to(message, "Ramadon Haqida: https://youtu.be/QG1NYPWjBT0")
    bot.reply_to(message, "Ramadon Haqida: https://youtu.be/GyhX6p_6XjU")


@bot.message_handler(commands=["salovatlar"])
def salovat(message):
    bot.reply_to(message, "Salovatlar: @iMusics_Bot");


@bot.message_handler(commands=['java'])
def java(message):
    bot.reply_to(message, "https://youtu.be/eIrMbAQSU34");

# def start(update, context):
#     update.message.reply_text("Assalomu alaykum, Hush Kelibsiz. 🥰");
#
# def help(update, context):
#     update.message.reply_text(
#         """
#         /start -> Welcome to the channel.😇
#         /help -> This praticular message.🥶
#         /vaqt -> About various vaqitlar of Simplilearn.🤝
#         /yana -> The frist vidio form ramadon playlist.🧠
#         /python -> The frist vidio from python playlist.👀
#         /java -> The frist vidio from java playlist.🎓
#         /contact -> contact infarmation.🌸
#         """
#     )
# def vaqt(update, context):
#     update.message.reply_text("Ramadon: https://www.islam.uz/vaqtlar/");

# def yana(update, context):
#     update.message.reply_text("Yana: https://www.islam.uz/vaqtlar/");
#
# def python(update, context):
#     update.message.reply_text("python: https://youtu.be/rfscVS0vtbw");
#
bot.polling();
bot.polling();
bot.polling();

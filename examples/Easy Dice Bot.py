import telebot
import time

# TOKEN
token = "<YOUR_API_TOKEN>"

# Call bot
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start'])
def benvenuto(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"HI! with /dice you can try your luck!") # Bot sends this message to the user

@bot.message_handler(commands=['dice'])
def dice(message):
    chat_id = message.chat.id
    bot.send_dice(chat_id, emoji="🎲")
    time.sleep(6) # Delay 6 Seconds
    bot.send_message(chat_id, f"Creator @FalcoAleDev") # After 6 Sec send this


bot.infinity_polling()

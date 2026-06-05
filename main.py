import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Assalom alaykum, meni portfolio botimizga xush kelibsiz."
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("About me")
    btn2 = types.KeyboardButton("Contact")
    btn3 = types.KeyboardButton("Skills")
    btn4 = types.KeyboardButton("Projects")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.text == "About me":
#         bot.send_message(message.chat.id, "Men Asadbek Rakhimovman. \n Men frontend engineerman")
#     elif message.text == "Contact":
#         bot.send_message(message.chat.id, "Bu qism tez orada qo'shiladi")

@bot.message_handler(func=lambda message: message.text == "About me")
def aboutme_handler(message):
    text = "💼 3+ yil davomida production-grade web ilovalar yaratib kelmoqdaman. " \
    "\n⚡React.js, Next.js, TypeScript va zamonaviy frontend arxitekturasi bo'yicha tajribam bor. " \
    "\n🌱 Hozirda React Native va Python backend yo'nalishlarini o'rganmoqdaman. " \
    "\n🧠 Performance optimization, clean architecture va maintainable UI sistemalarga qiziqaman. " \
    "\n💬 React, TypeScript, Next.js, Python va frontend system design bo'yicha suhbatlashishga doim tayyorman."

    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/asadbekjs")
    btn2 = types.InlineKeyboardButton("Linkedin", url="https://www.linkedin.com/in/asadbek-rakhimov")
    keyboard.add(btn1, btn2)

    text = "Men bilan bog'lanish uchun pastdagi linklarga bosing"

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Skills")
def skills_handler(message):
    text = (
        "🛠 *Tech Stack*\n"
        "━━━━━━━━━━━━━━━━\n\n"
        "🖥 *Frontend:*\n"
        "  • React.js, Next.js\n"
        "  • TypeScript, JavaScript\n\n"
        "🔄 *State Management:*\n"
        "  • Redux Toolkit\n"
        "  • TanStack Query\n\n"
        "🎨 *Styling:*\n"
        "  • Tailwind CSS\n"
        "  • Shadcn UI\n\n"
        "🗄 *Backend & DB:*\n"
        "  • Supabase\n"
        "  • Python (o'rganmoqdaman)\n\n"
        "🧰 *Tools:*\n"
        "  • Git, GitHub, VS Code\n"
        "  • Figma, Postman"
    )

    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "Projects")
def projects_handler(message):
    text = (
        "*Loyihalarim*\n"
        "- Kirildan lotinga/lotindan kirilga o'tkazuvchi telegram bot: [bot](https://t.me/cyrillic_to_latin_simple_bot)\n"
        "- Tibbiy yordam xizmati: [website](https://medical-assistance2.vercel.app)"
    )

    bot.send_message(message.chat.id, text, parse_mode="Markdown")

bot.infinity_polling()


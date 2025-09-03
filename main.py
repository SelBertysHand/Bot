from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

# Твой токен уже вставлен:
TOKEN = "8111857866:AAE1Nm5u2-h1mQPj-s4-nJtHVZX8kAP4X6Y"

# Эффект "Матрицы"
def matrix(update: Update, context: CallbackContext) -> None:
    symbols = "01"
    matrix_lines = []
    for _ in range(15):  # кол-во строк
        line = "".join(random.choice(symbols) for _ in range(30))
        matrix_lines.append(line)
    update.message.reply_text("\n".join(matrix_lines))

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Отправь /matrix и я покажу эффект Матрицы.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("matrix", matrix))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

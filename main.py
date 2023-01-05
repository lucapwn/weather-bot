# MIT License

# Copyright (c) 2023 Lucas Araújo

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, Filters, Updater
from dotenv import load_dotenv
from src import functions

def main():
    load_dotenv()
    
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    RAPID_API_TOKEN = os.getenv("RAPID_API_TOKEN")

    if None in (TELEGRAM_BOT_TOKEN, RAPID_API_TOKEN):
        print("Some of the tokens were not found. Check that the content of the .env file is correct.")
        sys.exit()

    try:
        updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    except Exception:
        print("Unable to connect to the bot! Check your connection and if the token is correct.")
        sys.exit()

    updater.dispatcher.add_handler(CallbackQueryHandler(functions.button, run_async=True))
    updater.dispatcher.add_handler(CommandHandler("start", functions.start, run_async=True))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, functions.message, run_async=True))

    print("Bot running! :)")

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

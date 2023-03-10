# Weather Bot

The [Weather Bot](https://github.com/lucapwn/weather-bot) is a bot on the Telegram platform designed to help you get real-time information about the weather in your city.

![Badge](https://img.shields.io/static/v1?label=license&message=MIT&color=1E90FF)
![Badge](https://img.shields.io/static/v1?label=build&message=passing&color=00d110)

## Content

- [About](#about)
- [Support](#support)
- [Setting](#setting)
  - [Getting the tokens](#getting-the-tokens)
  - [Saving the tokens](#saving-the-tokens)
- [Running](#running)
  - [Getting weather information](#getting-weather-information)
- [Screenshot](#screenshot)
- [Author](#author)
- [License](#license)

## About

The [Weather Bot](https://github.com/lucapwn/weather-bot) was developed in Python using the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library to perform integration with the [Telegram](https://telegram.org/) platform, thus enabling communication with all users in real time.

To get the weather information for the city in which the user reported to the bot, the [Visual Crossing Weather](https://rapidapi.com/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather/) API provided by [RapidAPI](https://rapidapi.com/) was used.

## Support

This software is available for Windows and GNU/Linux operating systems.

I have not been able to test it on macOS yet, but I believe it will work as well.

## Setting

To create the bot, it is necessary to have a [Telegram](https://telegram.org/) account. If you do not have an account, please create one.

To get the climate information, as mentioned above, we need to use an API. To do this, if you do not have a [RapidAPI](https://rapidapi.com/) account, please create one.

### Getting the tokens

After you have created the above accounts, let's create the bot itself. Inside Telegram, open a conversation with [@BotFather](https://t.me/BotFather) and create a bot with the command ```/newbot```. Next, enter the name and username of your bot.

https://user-images.githubusercontent.com/58787069/211084294-d790a93c-3e51-4b86-a71c-47372f0f9708.mp4

If all went well, you will receive a message with your bot's token similar to this one:

~~~bash
2763282781:AAEnulN_nH9f2Sr2j_vl5mi8Fw9XskzLf4s
~~~

Now, navigate to the [RapidAPI](https://rapidapi.com/) site, search for [Visual Crossing Weather](https://rapidapi.com/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather/) (or click next to it), and click "Subscribe to Test".

Finally, under "Header Parameters" you will see your X-RapidAPI-Key similar to this one:

~~~bash
4999cb7e22mkh7491sba992e1f76px63690jsnfedaeadzf15x
~~~

### Saving the tokens

After getting the tokens, we need to save them.

Create a file in the project root called ```.env``` and insert the content below:

~~~python3
TELEGRAM_BOT_TOKEN="2763282781:AAEnulN_nH9f2Sr2j_vl5mi8Fw9XskzLf4s"
RAPID_API_TOKEN="4999cb7e22mkh7491sba992e1f76px63690jsnfedaeadzf15x"
~~~

Note: Enter your real tokens, not the tokens in the example above.

## Running

Install the project dependencies:

~~~console
foo@bar:~$ pip3 install -r ./requirements.txt
~~~

Run the main file:

~~~console
foo@bar:~$ python3 ./main.py
~~~

If all goes well, you will see a success message. That's it! :)

### Getting weather information

Finally, inside [Telegram](https://telegram.org/), search for the username of the bot you created and send a message from your city name.

## Screenshot

The video below illustrates the conversation with the running Weather Bot.

https://user-images.githubusercontent.com/58787069/211088204-d4176c8d-f092-4066-87ee-3dbce16e24b5.mp4

## Author

Developed by [Lucas Ara??jo](https://github.com/lucapwn).

## License

This software is [MIT](https://choosealicense.com/licenses/mit/) licensed.

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
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    context.bot.send_chat_action(update.message.chat_id, "typing")

    keyboard = [
        [
            InlineKeyboardButton("How does it work?", callback_data="doubts")
        ],
        [
            InlineKeyboardButton("About me", callback_data="me"),
            InlineKeyboardButton("About my owner", callback_data="owner")
        ],
        [
            InlineKeyboardButton("⚙️ Support", url="https://linktr.ee/lucapwn")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    text = f"Hello, {update.message.from_user.first_name}. Welcome! 🤓\n\nI'm a bot made to help you analyze information about your city's weather. 🌦"
    update.message.reply_text(text, reply_markup=reply_markup)

def button(update, context):
    text = {
        "doubts": "I'm a bot made to help you analyze information about your city's weather. 🌦\n\nFor information about the climate in your city, just send me a message with the name of the city.\n\nNote: Just send me the name of the city.",
        "me": "I'm a bot made to help you analyze information about your city's weather. 🌦\n\nI was developed in Python for the purpose of helping you understand how I work. 🤓",
        "owner": "My owner is a guy who loves software development and hacking in general.\n\nWant to know more about him? 🤓\n\nhttps://linktr.ee/lucapwn\n\nGet in touch!",
        "return": f"Hello, {update.callback_query.from_user.first_name}. Welcome! 🤓\n\nI'm a bot made to help you analyze information about your city's weather. 🌦"
    }

    text = text[update.callback_query.data]

    keyboard = [
        [
            InlineKeyboardButton("« Return", callback_data="return")
        ]
    ]

    if update.callback_query.data == "return":
        keyboard = [
            [
                InlineKeyboardButton("How does it work?", callback_data="doubts")
            ],
            [
                InlineKeyboardButton("About me", callback_data="me"),
                InlineKeyboardButton("About my owner", callback_data="owner")
            ],
            [
                InlineKeyboardButton("⚙️ Support", url="https://linktr.ee/lucapwn")
            ]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id, reply_markup=reply_markup, disable_web_page_preview=True, text=text)

def get_weather(location):
    RAPID_API_TOKEN = os.getenv("RAPID_API_TOKEN")
    url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

    headers = {
        "X-RapidAPI-Key": RAPID_API_TOKEN,
        "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
    }

    params = {
        "aggregateHours": "12",
        "location": location,
        "contentType": "json",
        "unitGroup": "metric",
        "shortColumnNames": "0"
    }

    try:
        response = requests.get(url=url, headers=headers, params=params).json()
    except Exception:
        response = None

    return response

def validate(data):
    if data == " ":
        return None

    return data

def message(update, context):
    context.bot.send_chat_action(update.message.chat_id, "typing")

    location = update.message.text
    response = get_weather(location)

    if not response:
        text = "An error occurred while getting the data from the climate API."
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=text)
        return

    if "errorCode" in response:
        text = "This city could not be found. Please try again!"
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=text)
        return

    temperature            = validate(response["locations"][location]["values"][0]["temp"])
    minimum_temperature    = validate(response["locations"][location]["values"][0]["mint"])
    maximum_temperature    = validate(response["locations"][location]["values"][0]["maxt"])
    dew_point              = validate(response["locations"][location]["values"][0]["dew"])
    heat_index             = validate(response["locations"][location]["values"][0]["heatindex"])
    wind_chill             = validate(response["locations"][location]["values"][0]["windchill"])
    wind_direction         = validate(response["locations"][location]["values"][0]["wdir"])
    wind_speed             = validate(response["locations"][location]["values"][0]["wspd"])
    wind_gust              = validate(response["locations"][location]["values"][0]["wgust"])
    weather_preciptype     = validate(response["locations"][location]["values"][0]["preciptype"])
    chance_precipitation   = validate(response["locations"][location]["values"][0]["pop"])
    precipitation          = validate(response["locations"][location]["values"][0]["precip"])
    weather_severerisk     = validate(response["locations"][location]["values"][0]["severerisk"])
    weather_cape           = validate(response["locations"][location]["values"][0]["cape"])
    relative_humidity      = validate(response["locations"][location]["values"][0]["humidity"])
    cloud_cover            = validate(response["locations"][location]["values"][0]["cloudcover"])
    solar_energy           = validate(response["locations"][location]["values"][0]["solarenergy"])
    solar_radiation        = validate(response["locations"][location]["values"][0]["solarradiation"])
    ultraviolet_rays_level = validate(response["locations"][location]["values"][0]["uvindex"])
    snow                   = validate(response["locations"][location]["values"][0]["snow"])
    snow_depth             = validate(response["locations"][location]["values"][0]["snowdepth"])
    visibility             = validate(response["locations"][location]["values"][0]["visibility"])
    conditions             = validate(response["locations"][location]["values"][0]["conditions"])
    sea_level_pressure     = validate(response["locations"][location]["values"][0]["sealevelpressure"])
    latitude               = validate(response["locations"][location]["latitude"])
    longitude              = validate(response["locations"][location]["longitude"])
    timezone               = validate(response["locations"][location]["tz"])
    address                = validate(response["locations"][location]["address"])

    variables = [
        {"value": temperature,            "text": f"Temperature: {temperature} °C\n"},
        {"value": minimum_temperature,    "text": f"Minimum Temperature: {minimum_temperature} °C\n"},
        {"value": maximum_temperature,    "text": f"Maximum Temperature: {maximum_temperature} °C\n"},
        {"value": dew_point,              "text": f"Dew Point: {dew_point} °C\n"},
        {"value": heat_index,             "text": f"Heat Index: {heat_index} °C\n"},
        {"value": wind_chill,             "text": f"Wind Chill: {wind_chill} °C\n"},
        {"value": wind_direction,         "text": f"Wind Direction: {wind_direction}\n"},
        {"value": wind_speed,             "text": f"Wind Speed: {wind_speed} Kph\n"},
        {"value": wind_gust,              "text": f"Wind Gust: {wind_gust} Kph\n"},
        {"value": weather_preciptype,     "text": f"Weather Preciptype: {weather_preciptype}\n"},
        {"value": chance_precipitation,   "text": f"Chance Precipitation: {chance_precipitation}%\n"},
        {"value": precipitation,          "text": f"Precipitation: {precipitation} mm\n"},
        {"value": weather_severerisk,     "text": f"Weather Severerisk: {weather_severerisk}\n"},
        {"value": weather_cape,           "text": f"Weather Cape: {weather_cape}\n"},
        {"value": relative_humidity,      "text": f"Relative Humidity: {relative_humidity}%\n"},
        {"value": cloud_cover,            "text": f"Cloud Cover: {cloud_cover}\n"},
        {"value": solar_energy,           "text": f"Solar Energy: {solar_energy}\n"},
        {"value": solar_radiation,        "text": f"Solar Radiation: {solar_radiation}\n"},
        {"value": ultraviolet_rays_level, "text": f"Ultraviolet Rays Level: {ultraviolet_rays_level}\n"},
        {"value": snow,                   "text": f"Snow: {snow} cm\n"},
        {"value": snow_depth,             "text": f"Snow Depth: {snow_depth} cm\n"},
        {"value": visibility,             "text": f"Visibility: {visibility} Km\n"},
        {"value": conditions,             "text": f"Conditions: {conditions}\n"},
        {"value": sea_level_pressure,     "text": f"Sea Level Pressure: {sea_level_pressure} mbar\n"},
        {"value": latitude,               "text": f"Latitude: {latitude}\n"},
        {"value": longitude,              "text": f"Longitude: {longitude}\n"},
        {"value": timezone,               "text": f"Timezone: {timezone}\n"},
        {"value": address,                "text": f"Address: {address}\n"}
    ]

    text = "Enjoy the information about your city's climate! 🌦\n\n"

    for variable in variables:
        if variable["value"]:
            text += variable["text"]

    context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=text)

from aiogram import types, Dispatcher
from services.text_reformat_service import get_formatted_weather_forecast
from aiogram.filters import Command
from aiogram import F


async def start_command(message: types.Message):
    await message.reply("Напиши название города, чтобы узнать погоду.")


async def city_weather(message: types.Message):
    city = message.text
    weather_info = get_formatted_weather_forecast(city)
    if weather_info:
        await message.reply(weather_info)
    else:
        await message.reply("Не удалось получить информацию о погоде. Попробуйте снова.")


def register_handlers(dp: Dispatcher):
    # Регистрация хендлеров
    dp.message.register(start_command, Command("start"))
    dp.message.register(city_weather, F.text)
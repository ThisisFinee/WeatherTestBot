from services.weather_service import get_weather_info


def get_formatted_weather_forecast(city):
    data = get_weather_info(city)
    if data:
        # Текущая погода
        current_temp = data["current_weather"]["temperature"]
        windspeed = data["current_weather"]["windspeed"]

        # Дневной прогноз
        max_temp = data["daily"]["temperature_2m_max"][0]
        min_temp = data["daily"]["temperature_2m_min"][0]
        precipitation = data["daily"]["precipitation_sum"][0]
        snowfall = data["daily"]["snowfall_sum"][0]

        return (
            f"Погода в населённом пункте {city}:\n"
            f"Текущая температура: {current_temp}°C, ветер {windspeed} км/ч\n"
            f"Максимальная температура: {max_temp}°C\n"
            f"Минимальная температура: {min_temp}°C\n"
            f"Осадки: {precipitation} мм\n"
            f"Количество снежных осадков: {snowfall} мм"
        )
    else:
        return "Не удалось получить информацию о погоде. Попробуйте снова."

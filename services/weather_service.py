import requests
from services.coordinates_service import get_coordinates


def get_weather_info(city: str):
    coordinates = get_coordinates(city)
    if not coordinates:
        return None

    latitude, longitude = coordinates

    # Запрос к Open-Meteo API
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
        f"&current_weather=true&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,snowfall_sum,"
        "&timezone=auto"
    )

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

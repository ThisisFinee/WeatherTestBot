from geopy.geocoders import Nominatim


def get_coordinates(city: str):
    geolocator = Nominatim(user_agent="weather_bot")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None

from flask import current_app
from .weather import Weather

class WeatherService:

    def __init__(self):
        pass

    def requestLocation(self, weather: Weather, city, stateCode, countryCode):
        return weather.callLocation(city, stateCode, countryCode)

    def requestWeather(self, weather: Weather, lat, lon):
        if (lat == None) :
            return weather.callWeather(-22.1225, -51.3883)    
        return weather.callWeather(lat, lon)
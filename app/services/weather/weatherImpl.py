from .weather import Weather
from flask import current_app
import requests

class WeatherImpl(Weather):

    def getResponseDict(self, link) -> str:
        requestLocate = requests.get(link)
        return requestLocate.json()

    def callLocation(self, city, stateCode, countryCode):
        return self.getResponseDict(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{stateCode},{countryCode}&limit=1&appid={current_app.config['WEATHER_KEY']}")

    def callWeather(self, lat, lon):
        return self.getResponseDict(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={current_app.config['WEATHER_KEY']}&lang=pt_br&units=metric")
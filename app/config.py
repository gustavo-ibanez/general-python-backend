import os
from .services.exchangeRates.exchangeRatesImpl import ExchangeRatesImpl
from .services.exchangeRates.exchangeRatesMock import ExchangeRatesMock
from .services.weather.weatherImpl import WeatherImpl
from .services.weather.weatherMock import WeatherMock

class Config:
   
    KEY_EXCHANGE = None
    WEATHER_KEY = None
    #MONGO_URI = "mongodb://localhost:27017/mydatabase"  # pra rodar sem docker
    MONGO_URI = "mongodb://mongodb:27017/mydatabase"

class ProductionConfig(Config):
    KEY_EXCHANGE = "c951ea2aec424674b97331472ec1d9df"
    WEATHER_KEY = "828ac938d21e998eb81af74052f2bff7"

class TestingConfig(Config):
    KEY_EXCHANGE = ""
    WEATHER_KEY = ""

def get_config():
    env = os.getenv('FLASK_ENV', 'testing')
    if env == 'production':
        return ProductionConfig()    
    return TestingConfig()
    

def getExchangeRates():
    env = os.getenv('FLASK_ENV', 'testing')
    if env == 'production': 
        return ExchangeRatesImpl()
    return ExchangeRatesMock()

def getWeather():
    env = os.getenv('FLASK_ENV', 'testing')
    if env == 'production': 
        return WeatherImpl()
    return WeatherMock()
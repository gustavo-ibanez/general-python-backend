from abc import ABC, abstractmethod

class Weather(ABC):

    @abstractmethod
    def callLocation(self, city, stateCode, countryCode):
        pass

    @abstractmethod
    def callWeather(self, lat, lon):
        pass

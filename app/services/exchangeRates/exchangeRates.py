from abc import ABC, abstractmethod

class ExchangeRates(ABC):
    
    @abstractmethod
    def callCurrencies(self):
        pass

    @abstractmethod
    def callValues(self):
        pass


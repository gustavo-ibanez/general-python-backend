from flask import current_app
from .exchangeRates import ExchangeRates

class ExchangeRatesService:

    def __init__(self):
        pass

    def exchangeRates(self, currencyFrom, currencyTo, result):
        value1 = result['rates'][currencyFrom]
        value2 = result['rates'][currencyTo]
        result = round(value2/value1, 2)
        return {
            "from" : currencyFrom,
            "to" : currencyTo,
            "valor": result }
       
    def calcExchangeRates(self, exchangeRates: ExchangeRates, fromValue, toValue):
        
        result = exchangeRates.callValues()
        if (fromValue == None or fromValue == ""):
            return self.exchangeRates('USD', 'BRL', result)
        else :
            return self.exchangeRates(fromValue, toValue, result)

    def showAllCurrency(self, exchangeRates: ExchangeRates):
        result = exchangeRates.callCurrencies()
        return result

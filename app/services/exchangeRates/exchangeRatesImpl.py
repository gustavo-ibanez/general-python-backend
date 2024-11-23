from .exchangeRates import ExchangeRates
from flask import current_app
import requests

class ExchangeRatesImpl(ExchangeRates):

    def getResponseDict(self, link) -> str:
        requestLocate = requests.get(link)
        return requestLocate.json()

    def callValues(self):
        return self.getResponseDict(f"https://openexchangerates.org/api/latest.json?app_id={current_app.config['KEY_EXCHANGE']}")

    def callCurrencies(self):
        return self.getResponseDict(f"https://openexchangerates.org/api/currencies.json?app_id={current_app.config['KEY_EXCHANGE']}")
from flask import Blueprint, jsonify, request
from .exchangeRatesService import ExchangeRatesService
from app.config import getExchangeRates

exchangeRates_bp = Blueprint('exchangeRates', __name__)

@exchangeRates_bp.route('/', methods=['GET'])
def getLatest():
    fromValue = request.args.get('from', default = None, type = str)
    toValue = request.args.get('to', default = None, type = str)
    
    exchangeRatesService = ExchangeRatesService()
    dados = exchangeRatesService.calcExchangeRates(getExchangeRates(), fromValue, toValue)
    
    response = jsonify(dados)   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@exchangeRates_bp.route('/currencies', methods=['GET'])
def getCurrencies():

    exchangeRatesService = ExchangeRatesService()
    dados = exchangeRatesService.showAllCurrency(getExchangeRates())
    response = jsonify(dados)   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
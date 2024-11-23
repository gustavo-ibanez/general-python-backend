from flask import Blueprint, jsonify, request
from app.config import getWeather
from .weatherService import WeatherService

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/information', methods=['GET'])
def getInformation():
    lat = request.args.get('lat', default = None, type = float)
    lon = request.args.get('lon', default = None, type = float)

    weather = WeatherService()
    dados = weather.requestWeather(getWeather(), lat, lon)
    
    response = jsonify(dados)   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@weather_bp.route('/location', methods=['GET'])
def gelLocation():
    city = request.args.get('city', default = None, type = str)
    stateCode = request.args.get('stateCode', default = None, type = str)
    countryCode = request.args.get('countryCode', default = None, type = str)
    
    weather = WeatherService()
    dados = weather.requestLocation(getWeather(), city, stateCode, countryCode)
    
    response = jsonify(dados)   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
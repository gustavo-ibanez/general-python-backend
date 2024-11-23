from flask import Blueprint, jsonify, request
from app.config import getWeather
from .localidadeService import LocalidadeService

localidade_bp = Blueprint('localidade', __name__)

@localidade_bp.route('/paises', methods=['GET'])
def getInformation():
    localidade = LocalidadeService()
    dados = localidade.requestLocation()
    
    response = jsonify(dados)   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
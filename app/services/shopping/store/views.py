from flask import Blueprint, jsonify, request
from app.config import getWeather
from .storeService import StoreService
from app.utils.jsonResponseError import JsonError

store_bp = Blueprint('store', __name__)

@store_bp.route('/item', methods=['POST'])
def addItem():
    store = StoreService()
    jsonResponse = store.addItem(request.json)

    return jsonify(jsonResponse), 201

@store_bp.route('/list', methods=['GET'])
def getAll():
    store = StoreService()
    jsonResponse = store.getAll()

    return jsonify(jsonResponse), 200

@store_bp.route('/item/<id>', methods=['GET'])
def getItem(id):
    store = StoreService()
    jsonResponse = store.getItem(id)
    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@store_bp.route('/item/<id>', methods=['PUT'])
def updateItem(id):
    store = StoreService()
    jsonResponse = store.updateItem(id, request.json)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@store_bp.route('/item/<id>', methods=['DELETE'])
def deleteItem(id):
    store = StoreService()
    jsonResponse = store.deleteItem(id)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200


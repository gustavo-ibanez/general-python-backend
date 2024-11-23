from flask import Blueprint, jsonify, request
from app.config import getWeather
from .productService import ProductService
from app.utils.jsonResponseError import JsonError

product_bp = Blueprint('product', __name__)

@product_bp.route('/item', methods=['POST'])
def addItem():
    product = ProductService()
    jsonResponse = product.addItem(request.json)

    return jsonify(jsonResponse), 201

@product_bp.route('/list', methods=['GET'])
def getAll():
    product = ProductService()
    jsonResponse = product.getAll()

    return jsonify(jsonResponse), 200

@product_bp.route('/item/<id>', methods=['GET'])
def getItem(id):
    product = ProductService()
    jsonResponse = product.getItem(id)
    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@product_bp.route('/item/<id>', methods=['PUT'])
def updateItem(id):
    product = ProductService()
    jsonResponse = product.updateItem(id, request.json)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@product_bp.route('/item/<id>', methods=['DELETE'])
def deleteItem(id):
    product = ProductService()
    jsonResponse = product.deleteItem(id)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200


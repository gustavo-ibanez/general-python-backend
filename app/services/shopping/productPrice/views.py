from flask import Blueprint, jsonify, request
from app.config import getWeather
from .productPriceService import ProductPriceService
from app.utils.jsonResponseError import JsonError

productPrice_bp = Blueprint('productPrice', __name__)

@productPrice_bp.route('/item', methods=['POST'])
def addItem():
    productPrice = ProductPriceService()
    jsonResponse = productPrice.addItem(request.json)

    return jsonify(jsonResponse), 201

@productPrice_bp.route('/list', methods=['GET'])
def getAll():
    product_id = request.args.get('product_id')
    store_id = request.args.get('store_id')
    filter_query = create_filter(product_id=product_id, store_id=store_id)

    productPrice = ProductPriceService()
    jsonResponse = productPrice.getAll(filter_query)

    return jsonify(jsonResponse), 200

@productPrice_bp.route('/item/<id>', methods=['GET'])
def getItem(id):
    productPrice = ProductPriceService()
    jsonResponse = productPrice.getItem(id)
    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@productPrice_bp.route('/item/<id>', methods=['PUT'])
def updateItem(id):
    productPrice = ProductPriceService()
    jsonResponse = productPrice.updateItem(id, request.json)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@productPrice_bp.route('/item/<id>', methods=['DELETE'])
def deleteItem(id):
    productPrice = ProductPriceService()
    jsonResponse = productPrice.deleteItem(id)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

def create_filter(product_id=None, store_id=None):
    filter_query = {}
    if product_id:
        filter_query["product_id"] = product_id
    if store_id:
        filter_query["store_id"] = store_id
    return filter_query
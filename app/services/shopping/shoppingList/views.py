from flask import Blueprint, jsonify, request
from app.config import getWeather
from .shoppingListService import ShoppingListService
from app.utils.jsonResponseError import JsonError
from app.services.shopping.product.productService import ProductService

shoppingList_bp = Blueprint('shoppingList', __name__)

@shoppingList_bp.route('/item', methods=['POST'])
def addItem():

    product = ProductService().getItem(request.json.get("product_id"))
    if product == None:
        return JsonError("1", "Product does not exist").getJson(), 404

    shoppingList = ShoppingListService()
    jsonResponse = shoppingList.addItem(request.json)

    return jsonify(jsonResponse), 201

@shoppingList_bp.route('/list', methods=['GET'])
def getAll():
    shoppingList = ShoppingListService()
    jsonResponse = shoppingList.getAll()

    return jsonify(jsonResponse), 200

@shoppingList_bp.route('/item/<id>', methods=['GET'])
def getItem(id):
    shoppingList = ShoppingListService()
    jsonResponse = shoppingList.getItem(id)
    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@shoppingList_bp.route('/item/<id>', methods=['PUT'])
def updateItem(id):
    product = ProductService().getItem(request.json.get("product_id"))
    if product == None:
        return JsonError("1", "Product does not exist").getJson(), 404

    shoppingList = ShoppingListService()
    jsonResponse = shoppingList.updateItem(id, request.json)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200

@shoppingList_bp.route('/item/<id>', methods=['DELETE'])
def deleteItem(id):
    shoppingList = ShoppingListService()
    jsonResponse = shoppingList.deleteItem(id)

    if jsonResponse == None:
        return JsonError("1", "Item not found").getJson(), 404
    return jsonify(jsonResponse), 200


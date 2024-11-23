from flask import current_app
from app.extensions import mongo
from app.models.product_price import product_price_schema
from bson.objectid import ObjectId

class ProductPriceService:

    def __init__(self):
        pass

    def addItem(self, data):
        item = {
            "product_id": data.get("product_id"),
            "store_id": data.get("store_id"),
            "price": data.get("price")
        }
        result = mongo.db.product_price.insert_one(item)
        item["_id"] = str(result.inserted_id)
        return product_price_schema(item)
    
    def getAll(self, filter_query):
        items = mongo.db.product_price.find(filter_query)
        return [product_price_schema(item) for item in items]
    
    def getItem(self, id):
        item = mongo.db.product_price.find_one({"_id": ObjectId(id)})
        if item:
            return product_price_schema(item)
        return None
    
    def updateItem(self, id, data):
        updated_data = {
           "product_id": data.get("product_id"),
            "store_id": data.get("store_id"),
            "price": data.get("price")
        }
        result = mongo.db.product_price.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

        if result.matched_count == 1:
            return {"code": "0", 
                    "message": "Item updated successfully"}
        return None
    
    def deleteItem(self, id):
        result = mongo.db.product_price.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"code": "0", 
                    "message": "Item deleted successfully"}
        return None
from flask import current_app
from app.extensions import mongo
from app.models.product import product_schema
from bson.objectid import ObjectId

class ProductService:

    def __init__(self):
        pass

    def addItem(self, data):
        item = {
            "name": data.get("name").upper(),
            "description": data.get("description").upper() if data.get("description") else None
        }
        result = mongo.db.product.insert_one(item)
        item["_id"] = str(result.inserted_id)
        return product_schema(item)
    
    def getAll(self):
        items = mongo.db.product.find()
        return [product_schema(item) for item in items]
    
    def getItem(self, id):
        item = mongo.db.product.find_one({"_id": ObjectId(id)})
        if item:
            return product_schema(item)
        return None
        
    def updateItem(self, id, data):
        updated_data = {
            "name": data.get("name").upper(),
            "description": data.get("description").upper() if data.get("description") else None
        }
        result = mongo.db.product.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

        if result.matched_count == 1:
            return {"code": "0", 
                    "message": "Item updated successfully"}
        return None
    
    def deleteItem(self, id):
        mongo.db.shopping_list.delete_many({"product_id": id})
        mongo.db.product_price.find_one({"product_id": id})
        
        result = mongo.db.product.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"code": "0", 
                    "message": "Item deleted successfully"}
        return None
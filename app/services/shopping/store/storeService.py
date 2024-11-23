from flask import current_app
from app.extensions import mongo
from app.models.store import store_schema
from bson.objectid import ObjectId

class StoreService:

    def __init__(self):
        pass

    def addItem(self, data):
        item = {
            "name": data.get("name").upper()
        }
        result = mongo.db.store.insert_one(item)
        item["_id"] = str(result.inserted_id)
        return store_schema(item)
    
    def getAll(self):
        items = mongo.db.store.find()
        return [store_schema(item) for item in items]
    
    def getItem(self, id):
        item = mongo.db.store.find_one({"_id": ObjectId(id)})
        if item:
            return store_schema(item)
        return None
        
    def updateItem(self, id, data):
        updated_data = {
            "name": data.get("name").upper()
        }
        result = mongo.db.store.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

        if result.matched_count == 1:
            return {"code": "0", 
                    "message": "Item updated successfully"}
        return None
    
    def deleteItem(self, id):
        mongo.db.product_price.find_one({"store_id": id})
        
        result = mongo.db.store.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"code": "0", 
                    "message": "Item deleted successfully"}
        return None
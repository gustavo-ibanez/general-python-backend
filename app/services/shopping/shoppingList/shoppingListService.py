from flask import current_app
from app.extensions import mongo
from app.models.shopping_list import shopping_list_schema
from bson.objectid import ObjectId

class ShoppingListService:

    def __init__(self):
        pass

    def addItem(self, data):
        item = {
            "product_id": data.get("product_id"),
            "quantity": data.get("quantity"),
            "purchased": data.get("purchased", False)  # Por padrão, 'purchased' será False
        }

        result = mongo.db.shopping_list.insert_one(item)
        item["_id"] = str(result.inserted_id)
        return shopping_list_schema(item)
    
    def getAll(self):
        items = mongo.db.shopping_list.find()
        return [shopping_list_schema(item) for item in items]
    
    def getItem(self, id):
        item = mongo.db.shopping_list.find_one({"_id": ObjectId(id)})
        if item:
            return shopping_list_schema(item)
        return None
        
    def updateItem(self, id, data):
        updated_data = {
            "product_id": data.get("product_id"),
            "quantity": data.get("quantity"),
            "purchased": data.get("purchased")
        }
        result = mongo.db.shopping_list.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

        if result.matched_count == 1:
            return {"code": "0", 
                    "message": "Item updated successfully"}
        return None
    
    def deleteItem(self, id):
        result = mongo.db.shopping_list.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"code": "0", 
                    "message": "Item deleted successfully"}
        return None
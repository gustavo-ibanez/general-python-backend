from bson.objectid import ObjectId

def shopping_list_schema(item):
    return {
        "_id": str(item["_id"]) if "_id" in item else None,
        "product_id": str(item["product_id"]) if "product_id" in item else None,
        "quantity": item["quantity"],
        "purchased": item["purchased"]
    }


       
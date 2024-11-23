from bson.objectid import ObjectId

def product_price_schema(item):
    return {
        "_id": str(item["_id"]) if "_id" in item else None,
        "product_id": str(item["product_id"]) if "product_id" in item else None,
        "store_id": str(item["store_id"]) if "store_id" in item else None,
        "price": item["price"]
    }
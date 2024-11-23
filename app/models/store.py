from bson.objectid import ObjectId

def store_schema(item):
    return {
        "_id": str(item["_id"]) if "_id" in item else None,
        "name": item["name"]
    }
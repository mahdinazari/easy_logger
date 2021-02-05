from pymongo import MongoClient


class MycolRepository(object):
    def __init__(self):
        mongo_client = MongoClient('localhost', 27017)
        database = mongo_client.flask
        self.collection = database.mycol

    def to_dict(self, data_source):
        result = []
        for i in data_source:
            result.append(i)

        return result

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def insert_many(self, data):
        return self.collection.insert_many(data)

    def find_all(self, conditions=None, fields=None, skip=0, limit=0):
        collection = self.collection
        result = collection \
            .find(conditions, fields) \
            .skip(int(skip)) \
            .limit(int(limit))
        return self.to_dict(result)

    def find_one(self, conditions=None):
        collection = self.collection
        result = collection.find_one(conditions)
        return result

    def delete_one(self, conditions):
        collection = self.collection
        return collection.delete_one(conditions)

    def delete_many(self, conditions):
        collection = self.collection
        return collection.delete_many(conditions)

    def delete_all(self):
        collection = self.collection
        result = collection.delete_many({})
        return result

    def update_one(self, conditions, new_value):
        collection = self.collection
        return self.collection.update_one(conditions, new_value)

    def update_many(self, conditions, new_value):
        collection = self.collection
        return self.collection.update_many(conditions, new_value)


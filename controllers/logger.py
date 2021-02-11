from uuid import uuid4
from datetime import datetime

from pymongo import MongoClient

from application.config import Config


class Logger(object):
    def __init__(self, log):
        mongo_client = MongoClient('localhost', 27017)
        database = mongo_client[Config.LOGGER_DATABASE]
        self.collection = database[Config.LOGGER_COLLECTION]
        self.log = {
            "_id": str(uuid4()),
            "action": log.action if log.action else None,
            "actor": log.actor if log.actor else None,
            "level": log.level if log.level else None,
            "code": log.code if log.code else None,
            "message": log.message if log.message else None,
            "_input": log._input if log._input else None,
            "_output": log._output if log._output else None,
            "created_at": datetime.now().isoformat(),
        }

    def to_dict(self, data_source):
        result = []
        for i in data_source:
            result.append(i)

        return result

    def insert_one(self):
        return self.collection.insert_one(self.log)

    def insert_many(self, data):
        return self.collection.insert_many(self.log)

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


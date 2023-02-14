#!/usr/bin/env python3
"""Lists all documents from mongodb using pymongo"""


def list_all(mongo_collection):
    """ List all documents from the mongodb database """
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []

    return docs

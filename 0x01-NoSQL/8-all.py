#!/usr/bin/env python3
"""Lists all documents from mongodb using pymongo"""


def list_all(mongo_collection):
    """ List all documents from the mongodb database """
    return [doc for doc in mongo_collection.find()]

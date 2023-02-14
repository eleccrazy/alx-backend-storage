#!/usr/bin/env python3
"""A python script that interacts with the mongodb database"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    query = {"name": name}
    new = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new)

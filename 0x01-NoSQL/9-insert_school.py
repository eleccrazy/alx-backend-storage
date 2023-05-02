#!/usr/bin/env python3
"""Python script that interacts with mongodb"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document to the collection"""
    return mongo_collection.insert_one(kwargs).inserted_id

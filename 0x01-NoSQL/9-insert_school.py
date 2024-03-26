#!/usr/bin/env python3
"""Module for using pymongo """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: keyword arguments.

    Returns:
        The new _id.
    """
    id_obj = mongo_collection.insert_one(kwargs)
    return id_obj.inserted_id

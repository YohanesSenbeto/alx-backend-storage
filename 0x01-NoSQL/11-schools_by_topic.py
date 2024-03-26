#!/usr/bin/env python3

"""Write a Python function that returns the list"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of school documents containing the specified topic.
    """
    # Find documents that contain the specified topic
    schools = mongo_collection.find({"topics": topic})
    return list(schools)

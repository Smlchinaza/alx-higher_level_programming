#!/usr/bin/python3
 """
    Returns a dictionary description with a simple data structure
    for JSON serialization of an object
    """

def class_to_json(obj):
    """
    Returns a dictionary description with a simple data structure
    for JSON serialization of an object
    """
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(element) for element in obj]
    elif isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj
    else:
        attributes = {}
        for attr in dir(obj):
            if not attr.startswith("__") and not callable(getattr(obj, attr)):
                attributes[attr] = class_to_json(getattr(obj, attr))
        return attributes

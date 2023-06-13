#!/usr/bin/python3
""" ..............................
"""


def class_to_json(obj):
    """................................."""

    respond = {}
    if hasattr(obj, "__dict__"):
        respond = obj.__dict__.copy()
    return respond

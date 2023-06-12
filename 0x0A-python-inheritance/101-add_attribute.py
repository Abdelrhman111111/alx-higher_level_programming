#!/usr/bin/python3
""" ............................ """


def add_attribute(prmObject, prmName, prmValue):
    """ ...................... """
    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(prmObject, prmName)):
        prmObject.__setattr__(prmName, prmValue)

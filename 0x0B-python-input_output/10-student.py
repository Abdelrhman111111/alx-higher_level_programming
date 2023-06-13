#!/usr/bin/python3
""" ............................
"""


class Student:
    """..............................."""

    def __init__(self, first_name, last_name, age):
        """ ....................... """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ ........................"""
        objec = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return objec

            dlist = {}

            for iatr in range(len(attrs)):
                for satr in objec:
                    if attrs[iatr] == satr:
                        dlist[satr] = objec[satr]
            return dlist

        return objec

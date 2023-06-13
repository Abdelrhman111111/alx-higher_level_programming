#!/usr/bin/python3
"""..........."""


import json
import sys
import os.path

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

file_name = "additem.json"
if os.path.isfile(file_name):
    objec = load(file_name)
else:
    objec = []
obj.extend(sys.argv[1:])
save(objec, file_name)

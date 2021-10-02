#!/usr/bin/python3
""" add as many arguments into a list in json file """

import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

file_name = "add_item.json"

try:
    list = load_from_json_file(file_name)
except:
    list = []

for argument in sys.argv[1:]:
    list.append(argument)

save_to_json_file(list, file_name)

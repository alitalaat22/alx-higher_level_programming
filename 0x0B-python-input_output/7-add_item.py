#!/usr/bin/python3
""" Script that adds all arguments to
a Python list and saves them to a JSON file
"""


from genericpath import exists
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
# Check if the file exists
if exists(filename):
    # Load existing data from the file
    mylist = load_from_json_file(filename)
else:
    # Check if the file exists
    mylist = []

# Add command-line arguments to the list (excluding the script name itself)
args = sys.argv[1:]
mylist.extend(args)

# Save the updated list back to the file
save_to_json_file(mylist, filename)

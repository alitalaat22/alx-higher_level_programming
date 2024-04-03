#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = map(lambda s: replace if s == search else s, my_list)
    return list(result)

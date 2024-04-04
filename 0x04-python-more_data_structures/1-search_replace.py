# #!/usr/bin/python3
# def search_replace(my_list, search, replace):
#     result = map(lambda s: replace if s == search else s, my_list)
#     return list(result)

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    s = []
    n = []
    for i in my_list:
        if i == search:
            n.append(replace)
            s.append(n)
            return s
        else:
            return
    else:
        return my_list

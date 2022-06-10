#!/usr/bin/python3
def uniq_add(my_list=[]):
    ls = []
    for i in my_list:
        if i not in ls:
            ls.append(i)
    return sum(ls)

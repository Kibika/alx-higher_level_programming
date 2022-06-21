#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        index = 0
        while index < x:
            print("{:d}".format(my_list[index], end=""))
            index += 1
    except TypeError as err:
        print(err)
    else:
        print("")
        return index

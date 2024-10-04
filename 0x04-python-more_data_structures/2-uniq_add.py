#!/usr/bin/python3
def uniq_add(my_list=[]):

    sum_num = 0 

    added_int = []

    for i in my_list:
        if i not in added_int:
            added_int.append(i)
            sum_num += i
    return sum_num

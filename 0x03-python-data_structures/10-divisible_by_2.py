#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_ = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            div_.append(True)
        else:
            div_.append(False)

    return (div_)

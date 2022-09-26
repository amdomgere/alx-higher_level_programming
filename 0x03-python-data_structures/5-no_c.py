#!/usr/bin/python3
def no_c(my_string):

    a = 0

    new_str = my_string[:]

    for i in range(len(my_string)):
        if (my_string[i] == 'C' or my_string[i] == 'c'):
            new_str = new_str[:(i - a)] + my_string[(i + 1):]
            a += 1

    return (new_str)

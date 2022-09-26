#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)

    if len_s == 0:
        new_tuple = (len_s, None)
    else:
        new_tuple = (len_s, sentence[0])

    return (new_tuple)

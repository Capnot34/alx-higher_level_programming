#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total, weights = 0, 0
    for (score, weight) in my_list:
        total += score * weight
        weights += weight
    return total / weights


from math import *

def func_1(value):
    result_1 = floor(sqrt(abs(value)))
    result_2 = ceil(sqrt(abs(value)))
    return result_1, result_2


print(func_1(int(input())))
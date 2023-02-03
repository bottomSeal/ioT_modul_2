from math import *

def func_1(b):
    z = (cos((3/8)*pi - b/4))**2 - (cos((11/8)*pi + b/6))**2
    return z


print(func_1(int(input())))
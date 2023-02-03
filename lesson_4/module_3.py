from random import randint

__name__ == "module_2"

def lst_generator(n):
    lst = [randint(0, 1000) for _ in range(n)]
    return lst
    
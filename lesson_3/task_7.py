import math


def taxi_cost(distance):
    cost = 50 + 25 * math.ceil(distance / 500)
    return cost


print(taxi_cost(12))
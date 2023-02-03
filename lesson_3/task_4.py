def decree_generator(num_degrees, number):
    lst = [number ** i for i in range(num_degrees)]
    return lst


print(decree_generator(number=2, num_degrees=6))

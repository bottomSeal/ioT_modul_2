def primary_check(value):
    num_of_div = 0
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            num_of_div += 1
    if num_of_div == 1:
        print(f"Число {value} является простым.")
    else:
        print(f"Число {value} не является простым.")


primary_check(7)
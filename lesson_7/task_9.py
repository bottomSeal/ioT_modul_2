from random import randint

digits_lst = []
while len(digits_lst) != 6:
    digit = randint(1, 49)
    if digit not in digits_lst:
        digits_lst.append(digit)
        
print(sorted(digits_lst))
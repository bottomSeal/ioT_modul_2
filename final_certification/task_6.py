import random

special_symbols = "@%/!"
letters = "qwerty"
numbers = "12345"

lst = [special_symbols, letters, numbers]
random.shuffle(lst)

password = random.choice(lst[0]) + random.choice(lst[1]) + random.choice(lst[2])
print(password)
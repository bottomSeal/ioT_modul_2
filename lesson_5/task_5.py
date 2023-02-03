from random import randint

file = open("lesson_5\\random_numbers.txt", "w")

for _ in range(10):
    for i in range(10):
        file.write(f"{randint(10, 100)} ")
    file.write("\n")
    
file.close()
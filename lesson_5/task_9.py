import csv

file = open ("lesson_5\\Books.csv", "a") 
n = int(input("Введите количество записей, которые нужно добавить: "))
for i in range(n):
    name = input("Введите название произведения: ") 
    author = input("Введите имя автора: ") 
    year = input("Введите год написания: ") 
    newRecord = name + ", " + author + ", " + year + "\n" 
    file.write(str(newRecord)) 
file.close()
author = input("Введите имя автора, произведения которого нужно найти: ")
file = open ("lesson_5\\Books.csv", "r") 
reader = csv.reader(file) 
count = 0
for row in file: 
    if author in str(row): 
        print(row) 
        count += 1
file.close()
if count == 0:
    print("Нет произведений этого автора.")
import csv

file = open ("lesson_5\\Books.csv", "r") 
start_year = int(input("Введите начало временного отрезка: "))
end_year = int(input("Введите окончание временного отрезка: "))
reader = csv.reader(file) 
for row in file: 
    if start_year <= int(row[-5:-1]) <= end_year:
        print(row)
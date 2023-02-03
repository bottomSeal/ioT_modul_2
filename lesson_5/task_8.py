import csv

file = open ("lesson_5\\Books.csv", "a") 
name = input("Enter name: ") 
author = input("Enter author: ") 
year = input("Enter year: ") 
newRecord = name + ", " + author + ", " + year + "\n" 
file.write(str(newRecord)) 
file.close() 
file = open ("lesson_5\\Books.csv", "r") 
for row in file: 
    print(row) 
file.close() 
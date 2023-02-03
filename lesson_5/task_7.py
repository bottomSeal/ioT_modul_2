import csv


file = open ("lesson_5\\Books.csv", "w") 
newRecord_1 = "Война и мир, Лев Толстой, 1865\n"
newRecord_2 = "Ревизор, Николай Гоголь, 1836\n"
newRecord_3 = "Отцы и дети, Иван Тургенев, 1860\n"
newRecord_4 = "Мастер и Маргарита, Михаил Булгаков, 1940\n"
newRecord_5 = "Тихий Дон, Михаил Шолохов, 1940\n"
file.write(str(newRecord_1 + newRecord_2 + newRecord_3 + newRecord_4 + newRecord_5)) 
file.close() 
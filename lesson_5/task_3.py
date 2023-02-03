file = open("lesson_5\\Names.txt", "r") 
lst = [i[:len(i)-1] for i in file]
file.close()
print(lst)
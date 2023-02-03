input_file_name = input("Введите название файла, из которого нужно считать (в формате .txt): ")
file = open(f"lesson_7\\{input_file_name}", "r") 
lst = [i[:len(i)-1] for i in file]
file.close()

output_file_name = input("Введите название файла, в который нужно записать (в формате .txt): ")
file = open(f"lesson_7\\{output_file_name}", "w") 
for i in range(len(lst)):
    file.write(f"{i}: {lst[i]}\n")
file.close()
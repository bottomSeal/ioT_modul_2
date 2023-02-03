lst = [i for i in range(2, 17) if i % 2 == 0]
input_value = int(input("Введите множитель: "))
new_lst = [i * input_value for i in lst]
print(new_lst)
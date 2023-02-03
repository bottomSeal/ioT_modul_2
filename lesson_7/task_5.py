input_value = input()
flag = False
for i in range(len(input_value)):
    if input_value[i] != input_value[-i-1]:
        print("Не является палиндромом")
        flag = True
        break
if not flag:
    print("Палиндромом")
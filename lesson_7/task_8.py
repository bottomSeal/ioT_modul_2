password = input()
flag = False
if (len(password) == 8) and (password.upper() != password) and (password.lower() != password):
    for i in password:
        if i.isdigit():
            flag = True
            break

if flag:
    print("Пароль безопасен")
else:
    print("Пароль не достаточно безопасен")
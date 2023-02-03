name = input()
email = input()
password = input()
if not str.isalpha(name):
    print("Имя состоит не только из букв")
if "@" not in email:
    print("Адресс электронной почты должен содержать знак '@'")
if len(password) < 5:
    print("Пароль должен быть длинее 5 символов")
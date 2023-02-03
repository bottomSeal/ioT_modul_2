n = int(input("Введите количество чисел: "))
count = 0
for _ in range(n):
    number = int(input("Введите число: "))
    if -3.5 <= number <= 7.5:
        count += 1
print(f"Чисел из диапазона: {count}")
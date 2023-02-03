input_value = int(input())

for i in range(input_value):
    if 2 ** i < input_value:
        continue
    elif 2 ** i == input_value:
        print(f"Число {input_value} является степенью двойки.")
        break
    else:
        print(f"Число {input_value} не является степенью двойки.")
        break

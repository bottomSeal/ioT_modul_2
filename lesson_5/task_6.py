file = open("lesson_5\\random_numbers.txt", "r")

sum_lst = []
for i in file.readlines():
    sm = 0
    for j in range(len(i.split(" ")) - 1):
        sm += int(i.split(" ")[j])
    sum_lst.append(sm)

print(sum_lst)
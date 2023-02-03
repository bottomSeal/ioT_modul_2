import random

st = set([random.randint(-100-i, 100+i) for i in range(11)])
print(st)

print("Введите элементы которые нужно удалить: ")
for i in range(3):
    remove_elem = int(input())
    st.remove(remove_elem)

print(st)
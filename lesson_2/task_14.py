##lst = [int(input()) for i in range(10)]

##print(f"Количество неповторяющихся чисел: {len(set(lst))}\nМножество: {set(lst)}\nДлина множества {len(set(lst))}")

st = {}
for i in range(10):
    st.add(int(input()))

print(f"Множество: {st}\nДлина множества {len(st)}")
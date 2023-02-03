print("C   |  F")
for i in range(0, 101, 10):
    print(i, (3-len(str(i)))*" " + "|", 32+(i//10)*18)
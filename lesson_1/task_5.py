sec = int(input())

hours = sec // 3600
minutes = sec // 60 % 60
sec %= 60
print(hours, minutes, sec, sep=":")

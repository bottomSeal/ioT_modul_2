vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']


def num_vowel_letters(string):
    count = 0
    for i in string:
        if i in vowel_letters:
            count += 1
    return count


print(num_vowel_letters("влфыфлыовфлфы".lower()))
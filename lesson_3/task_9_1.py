vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']


def num_vowel_letters(string):
    vowel_letters_dict = {'а': 0, 'у': 0, 'о': 0, 'ы': 0, 'и': 0, 'э': 0, 'я': 0, 'ю': 0, 'ё': 0, 'е': 0}
    for i in string:
        if i in vowel_letters:
            vowel_letters_dict[i] += 1
    return vowel_letters_dict


print(num_vowel_letters("фЫваааозйцучи".lower()))
vowel_letters = ["a", "e", "i", "o", "u"]
input_value = input()
if input_value in vowel_letters:
    print("Буква гласная")
elif input_value == "y":
    print("Буква может быть как гласной, так и согласной")
else:
    print("Буква согласная")
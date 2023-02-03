print("Make a selection 1, 2 or 3:\n" +
      "1) Create a new file\n" +
      "2) Display the file \n" +
      "3) Add a new item to the file")

input_value = input()
if input_value == "1":
    subject = input("Enter name of the subject: ")
    file = open("lesson_5\\Subject.txt", "w")
    file.write(subject)
    file.close()
elif input_value == "2":
    file = open("lesson_5\\Subject.txt", "r")
    print(file.read())
    file.close()
elif input_value == "3":
    file = open("lesson_5\\Subject.txt", "a")
    subject = input("Enter name of the subject: ")
    file.write(subject)
    file.close()
else:
    print("Error. Incorrect number of command.")

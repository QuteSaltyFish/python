filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love making games.\n")
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divided by zero!")

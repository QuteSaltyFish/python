# message = input("Tell me something and I will speak back to U:")
# print("Hello, " + message + "!")
prompt = "\nPls enter the name of city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)"
active = True
while True:
    name = input(prompt)
    if name == 'quit':
        break
    else:
        print("I'd love to go to " + name.title() + "!")

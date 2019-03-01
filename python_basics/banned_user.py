banned_users = ['andrew', 'carolina', 'david']
user = input("What's your name?")
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + ", you Are Banned!")
requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']
for x in requested_toppings:
    print("Adding" + x)
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
print("\nFinished making your pizza!")

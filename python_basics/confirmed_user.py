unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifing user: "+current_user.title())
    confirmed_users.append(current_user)
confirmed_users.reverse()
print("\nThe following users are verified:")
for user in confirmed_users:
    print(user.title())

import json


def get_stored_name():
    """Get the stored name if it's available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """prompt for a new username"""
    username = input("What's your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(f_obj, username)
    return username


def greet_user():
    """Greet the user"""
    # Load the username, if it has been stored previously.
    #  Otherwise, prompt for the username and store it.
    username = get_stored_name()
    if username:
        print("Welcome back! " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")


greet_user()

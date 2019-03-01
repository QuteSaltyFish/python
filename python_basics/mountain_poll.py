responses = {}

# set a flag to indicate the polling is active
polling_active = True
while polling_active:
    # Prompt for names and response
    name = input("What's your name?")
    response = input("Which mountain would you like to climb someday?")

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another people to answer? (Yes/No)")
    if repeat.lower() == 'no':
        polling_active = False

# polling is completed, show the results
print("\n---Polling Results---")
for name, response in responses.items():
    print(name + " would like to climb" + response + ".")

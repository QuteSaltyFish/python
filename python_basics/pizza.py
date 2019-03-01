def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-" + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# # putting a list inside a Dictionary
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

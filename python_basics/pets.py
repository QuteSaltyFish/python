def describe_pet(animal_type='dog', pet_name='a'):
    """Display information about a pet."""
    print("\nIhave a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='c')
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

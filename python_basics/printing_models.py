def print_model(unprinted_designs, completed_models):
    """
    Simulat printing each design, until none are left, 
    Move each design to completed_models after printing.
    """
    # Simulate printing each design, until none are left
    # Move each design to completed_models after printing.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3d print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):

    # Display all completed_models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_model(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

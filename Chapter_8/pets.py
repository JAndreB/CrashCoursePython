def describe_pet(animal_type, pet_name='jerry'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()} is named {pet_name.title()}")

describe_pet('gerbil', 'dennis')
describe_pet('jeff', 'dog')
describe_pet(animal_type='whale', pet_name="mike")
describe_pet(animal_type='james')
describe_pet('mike')
"""A simple module to represent a restaurant"""

class restaurant:
    """A simple class to model a restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """describe the name a cuisine of the restaurant"""
        print(f"\nThe restaurant's name is {self.name}.")
        print(f"The restaurant's cuisine is {self.cuisine}.")

    def open_restaurant(self):
        """Simulate the opening of the restaurant"""
        print(f"\nThe resturant {self.name} is opening now.")
    
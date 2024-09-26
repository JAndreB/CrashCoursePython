class restaurant:
    """A simple class to model a restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 15

    def describe_restaurant(self):
        """describe the name a cuisine of the restaurant"""
        print(f"\nThe restaurant's name is {self.name}.")
        print(f"The restaurant's cuisine is {self.cuisine}.")

    def open_restaurant(self):
        """Simulate the opening of the restaurant"""
        print(f"\nThe resturant {self.name} is opening now.")
    
    def read_number_served(self):
        """Print the number of people this restaurant has served"""
        print(f"This restaurant has served {self.number_served} customers.")

    def set_number_served(self, new_number_served):
        """Set the number of customers served"""
        self.number_served = new_number_served

    def increment_number_served(self, customers):
        """Increment the number of customer served"""
        self.number_served += customers
    
    
Quillos = restaurant('Quillos', 'Mexican')
Barries = restaurant('Barries', 'Cajun')
Harmeens = restaurant('Harmeens', 'Indian')

Quillos.describe_restaurant()
Barries.describe_restaurant()
Harmeens.describe_restaurant()

Quillos.open_restaurant()
Quillos.set_number_served(14)
Quillos.read_number_served()
Quillos.increment_number_served(19)
Quillos.read_number_served()
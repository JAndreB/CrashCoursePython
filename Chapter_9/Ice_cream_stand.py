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
    

class Ice_cream_stand(restaurant):
    """A simple clas to model an ice cream stand"""

    def __init__(self, name):
        """Initialize attributes of the parent class"""
        super().__init__(name, cuisine='Ice Cream')
        self.flavours = ['vanilla', 'strawberry', 'chocolate']

    def show_flavours(self):
        """A method for showing flavours"""
        print(f"\nThe restaurant's flavour's are: ")
        for i in self.flavours:
            print(f"{i.title()}")
            

Ninas = Ice_cream_stand('Ninas')
Ninas.describe_restaurant()
Ninas.show_flavours()

"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    """A simple attempt to model a car battery for an electric car."""

    def __init__(self, battery=40):
        """Initialize the battery' attributes"""
        self.battery_size = battery
    
    def describe_battery(self):
        """Print a statement descibing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery!")
    
    def get_range(self):
        """Print the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
    
class ElectricCar(Car):
    """Represent the aspects of an electric car"""

    def __init__(self, make, model, year):
        """INitialize attibutes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()



class Car:
    """A simple attempt to model a car"""

    def __init__(self, make, model, year):
        """Initialize the attributes to descibe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """Print a statement showing the car's mileage"."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set odometer readiong to a given value
        Reject the change if it attemptes to roll; the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Odometer can not be rolled back.")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
class Battery:
    """A simple attempt to model a car battery for an electric car."""

    def __init__(self, battery=40):
        """Initialize the battery' attributes"""
        self.battery_size = battery
    
    def describe_battery(self):
        """Print a statement descibing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery!")

    def upgrade_battery(self, battery_size = 65):
        """initialize the upgraded battery size"""
        self.battery_size = battery_size
    
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





my_leaf = ElectricCar('nissan', 'leaf', '2024')
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
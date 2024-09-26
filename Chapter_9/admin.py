class User:
    """A basic class to simulate a user."""

    def __init__(self, first_name, last_name, dob, location):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.location = location

    def describe_user(self):
        """A function that describes the user"""

        print(f"\nThe user's first name is {self.first_name}.")
        print(f"The user's last name is {self.last_name}.")
        print(f"The user's date of birth is {self.dob}.")
        print(f"The user's location is {self.location}.")

    def greet_user(self):
        """A function simulating a greeting"""

        print(f"\ngreetrings {self.first_name}!")

class Privileges:
    """Initialize the privileges class"""
    def __init__(self, privileges = ['can post', 'can delete posts', 'can ban users']):
        self.privileges = privileges
    
    def show_privileges(self):
        """A class to show the list of privileges"""
        print(f"\nAdmin can do the following: ")
        for i in self.privileges:
            print(f"{i.title()}")



class Admin(User):
    """A simple class to model an admin user"""
    def __init__(self, first_name, last_name, dob, location):
        super().__init__(first_name, last_name, dob, location)
        self.privileges = Privileges()
    
    

user_1 = User("Maggie", "Wei", "15/12/2010", "LA")
user_2 = User("Yandes", "Toloubere", "15/6/2002", "UK")
user_3 = User("John", "Smith", "19/11/2001", "SA")
user_4 = User("Kid", "Bailag", "13/05/1995", "Phillipines")

user_5 = Admin("anders", 'onis', "13/12/43", "LDN")
user_5.privileges.show_privileges()


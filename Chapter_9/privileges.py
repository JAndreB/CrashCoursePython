"""A module to model an admin user"""

from user import User

class Admin(User):
    """A simple class to model an admin user"""
    def __init__(self, first_name, last_name, dob, location):
        super().__init__(first_name, last_name, dob, location)
        self.privileges = Privileges()



class Privileges:
    """Initialize the privileges class"""
    def __init__(self, privileges = ['can post', 'can delete posts', 'can ban users']):
        self.privileges = privileges
    
    def show_privileges(self):
        """A class to show the list of privileges"""
        print(f"\nthis admin can do the following: ")
        for i in self.privileges:
            print(f"{i.title()}")
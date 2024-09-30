"""A module to model a user"""

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

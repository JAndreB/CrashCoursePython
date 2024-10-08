class User:
    """A basic class to simulate a user."""

    def __init__(self, first_name, last_name, dob, location):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """A function that describes the user"""

        print(f"\nThe user's first name is {self.first_name}.")
        print(f"The user's last name is {self.last_name}.")
        print(f"The user's date of birth is {self.dob}.")
        print(f"The user's location is {self.location}.")

    def greet_user(self):
        """A function simulating a greeting"""

        print(f"\ngreetrings {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\nLogin attempts have been reset to 0")

    def print_login_attempts(self):
        print(f"\n{self.first_name} has made {self.login_attempts} attempts to log in.")

user_1 = User("Maggie", "Wei", "15/12/2010", "LA")
user_2 = User("Yandes", "Toloubere", "15/6/2002", "UK")
user_3 = User("John", "Smith", "19/11/2001", "SA")
user_4 = User("Kid", "Bailag", "13/05/1995", "Phillipines")

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()
user_4.describe_user()

user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()

user_4.print_login_attempts()
user_4.reset_login_attempts()
user_4.print_login_attempts()


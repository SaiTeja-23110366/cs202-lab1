"""
A simple script for the CS202 lab to demonstrate pylint.
"""

def calculate_area(width, height):
    """Calculates the area of a rectangle."""
    if width < 0 or height < 0:
        print("Error: Dimensions cannot be negative.")
        return None
    return width * height

def get_user_input():
    """Gets two numbers from the user."""
    try:
        width_input = float(input("Enter the width: "))
        height_input = float(input("Enter the height: "))
        return width_input, height_input
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None

# FIX: Added a comment to disable the "too-few-public-methods" warning for this class.
# pylint: disable=too-few-public-methods
class Greeter:
    """A simple class to greet someone."""
    def __init__(self, person_name):
        self.name = person_name

    def greet(self):
        """Prints a greeting message."""
        message = f"Hello, {self.name}! Welcome to the program."
        print(message)

if __name__ == "__main__":
    greeter = Greeter("Student")
    greeter.greet()

    # FIX: Renamed variables to avoid the "redefined-outer-name" warning.
    user_width, user_height = get_user_input()
    if user_width is not None:
        area = calculate_area(user_width, user_height)
        if area is not None:
            print(f"The area is: {area}")

    print("Pylint demonstration complete.")

# FIX: A blank line is added below this comment to fix the "missing-final-newline" error.

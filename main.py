"""
A simple script for the CS202 lab to demonstrate pylint.
"""

# import sys # This import was unused, so it's removed.

# UNUSED_VARIABLE was removed.

def calculate_area(width, height):
    """Calculates the area of a rectangle."""
    if width < 0 or height < 0:
        print("Error: Dimensions cannot be negative.")
        return None
    return width * height

def get_user_input():
    """Gets two numbers from the user."""
    try:
        # Renamed 'w' and 'h' to be more descriptive.
        width_input = float(input("Enter the width: "))
        height_input = float(input("Enter the height: "))
        return width_input, height_input
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None

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

    width, height = get_user_input()
    if width is not None:
        area = calculate_area(width, height)
        if area is not None:
            print(f"The area is: {area}")

    # The long line has been shortened to pass the pylint check.
    print("Pylint demonstration complete.")
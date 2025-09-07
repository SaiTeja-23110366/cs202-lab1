import sys

UNUSED_VARIABLE = "I am not used"

def calculate_area(width, height):
    """Calculates the area of a rectangle."""
    # This function is too simple, but good for a demo.
    if width < 0 or height < 0:
        print("Error: Dimensions cannot be negative.")
        return None
    return width * height

def get_user_input():
    """Gets two numbers from the user."""
    try:
        w = float(input("Enter the width: "))
        h = float(input("Enter the height: "))
        return w, h
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None

class Greeter:
    """A simple class to greet someone."""
    def __init__(self, person_name):
        self.name = person_name

    def greet(self):
        """Prints a greeting message."""
        # Using an f-string is a modern way to format strings.
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

    # This is an extra long line that pylint will complain about just for demonstration purposes.
    print("This concludes our simple demonstration program which was created for the CS202 lab assignment to show how pylint works with GitHub Actions.")

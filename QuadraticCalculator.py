import math


def quadratic_calculator(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Roots:", root1, root2)

    elif discriminant == 0:
        root = -b / (2 * a)
        print("Root:", root)

    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        print("Complex Roots:", root1, root2)


# Prompt the user for coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Call the function to calculate the roots of the quadratic function
quadratic_calculator(a, b, c)

"""In this script, we define the quadratic_calculator function that takes three coefficients (a, b, and c) as inputs. It calculates the discriminant of the quadratic equation (b^2 - 4*a*c) and then determines the type of roots based on the discriminant.

    If the discriminant is greater than 0, the quadratic equation has two distinct real roots, and they are calculated using the quadratic formula.
    If the discriminant is equal to 0, the quadratic equation has a single real root, and it is calculated.
    If the discriminant is less than 0, the quadratic equation has two complex roots, and they are calculated using complex numbers.

The calculated roots are then printed to the console.

To use the script, you'll be prompted to enter the coefficients a, b, and c for the quadratic equation. After entering the coefficients, the script will calculate and display the roots of the quadratic equation.

Note: This script uses the math module from the Python standard library for square root calculations."""
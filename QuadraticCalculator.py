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


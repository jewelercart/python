def even_odd_vending_machine(num):
    # Determine if input is even or odd
    if num % 2 == 0:
        print(f'{num} is an even number.')
        print('The next 9 even numbers are:')
        for i in range(1, 10):
            print(num + 2 * i)
    else:
        print(f'{num} is an odd number.')
        print('The next 9 odd numbers are:')
        for i in range(1, 10):
            print(num + 2 * i)

def main():
    while True:
        print("\nWelcome to the Even-Odd Vending Machine!")
        print("Enter a number to determine if it's even or odd and display the next 9 even or odd numbers.")
        print("Enter 'exit' to stop.")
        user_input = input("Your input: ")
        if user_input.lower() == 'exit':
            break
        elif not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        else:
            even_odd_vending_machine(int(user_input))

if __name__ == "__main__":
    main()

"""In this script, the even_odd_vending_machine function determines whether a 
given number is even or odd, and then prints the next 9 numbers of the same type. The main function is the user interaction loop, where the user can enter a number or choose to exit the program. 
The isdigit method is used to ensure the user entered a number."""
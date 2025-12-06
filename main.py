# Importing modules
import sys
import random

# Menu display function
def display_menu():
    print('\n1 - Generate a random number')
    print('0 - Exit')

# Range acquisition function
def get_range():
    while True:
        try:
            print('Select range:')
            min_number = int(input('Minimum value: '))
            max_number = int(input('Maximum value: '))

            if min_number > max_number:
                print('Error: The minimum number cannot be greater than the maximum!')
                continue

            generate_number(min_number, max_number)
            return
        except ValueError: 
            print('Error: Enter a number!')

# Random number generation function
def generate_number(min_val, max_val):
    while True:
        random_number = random.randint(min_val, max_val)
        print('Result:')
        print(f'Range: {min_val} - {max_val}')
        print(f'Random number: {random_number}\n')
        print('1 - Generate more')
        print('2 - Menu')
        print('0 - Exit')

        choice = input('\nSelect: ')
        if choice == '1':
            continue
        elif choice == '2':
            return
        elif choice == '0':
            sys.exit()

# Main function
def main():
    while True:
        print('=== Random Number Generator ===')
        display_menu()
        choice = input('\nSelect: ')
        if choice == '1':
            get_range()
        elif choice == '0':
            sys.exit()
        else:
            print('Invalid choice. Please try again.\n')

# Program entry point
if __name__ == "__main__":
    main()
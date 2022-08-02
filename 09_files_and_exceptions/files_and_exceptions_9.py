"""
0-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""
import json

def get_store_favourite_number():
    favourite_number = input("Please input your favourite number: ")
    with open('number.json', 'w') as file:
        json.dump(favourite_number, file)

def print_favourite_number():
    with open('number.json', 'r') as file:
        favourite_number = json.load(file)
    print('I know your favourite number! It\'s ' + favourite_number)

get_store_favourite_number()
print_favourite_number()

"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""

def get_stored_number():
    with open('number.json', 'r') as file:
        favourite_number = json.load(file)
    return favourite_number
def favourite_number():
    try:
        favourite_number = get_stored_number()
        print('I know your favourite number! It\'s ' + favourite_number)
    except FileNotFoundError:
        get_store_favourite_number()

favourite_number()
favourite_number()

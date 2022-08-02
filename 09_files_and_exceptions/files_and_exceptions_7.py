"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""

prompt_message = 'Please enter two numbers and I will add them:'
number_1_message = 'Please enter the first number: '
number_2_message = 'Please enter the second number: '
quit_message = 'Do you wish to continue? Please enter yes to continue and no to quit: '

while True:
    try:
        print(prompt_message)
        number_1 = int(input(number_1_message))
        number_2 = int(input(number_2_message))
        print(number_1 + number_2)
        quit = input(quit_message)

        if quit == 'no':
            break
    except ValueError:
        print('you cannot add strings!')


"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block
executes properly
"""

try:
    with open('cats.txt', 'r') as file:
        lines_cat = file.readlines()
    for line in lines_cat:
        print(line)
except FileNotFoundError:
    print('The file is missing')

try:
    with open('dgs.txt', 'r') as file:
        lines_dog = file.readlines()
    for line in lines_dog:
        print(line)
except FileNotFoundError:
    print('The file is missing')

"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""

def print_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            print(line)
    except FileNotFoundError:
        print('The file is missing.')

files = ['dogs.txt', 'cats.txt']
for file in files:
    print_lines(file)

def print_lines_fail_silent(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            print(line)
    except FileNotFoundError:
        pass

for file in files:
    print_lines_fail_silent(file)
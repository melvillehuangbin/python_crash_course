"""
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""
prompt_message = 'Please enter two numbers and I will add them:'
number_1_message = 'Please enter the first number: '
number_2_message = 'Please enter the second number: '

try:
    print(prompt_message)
    number_1 = int(input(number_1_message))
    number_2 = int(input(number_2_message))
    print(number_1 + number_2)
except ValueError:
    print('you cannot add strings!')


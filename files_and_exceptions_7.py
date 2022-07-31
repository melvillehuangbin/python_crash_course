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
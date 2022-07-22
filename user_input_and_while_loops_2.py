"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""
message = ""
while message != 'quit':
    message = input('Please enter a pizza topping, enter quit to exit ')

    if message != 'quit':
        print(message)

"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""
age = ""
while age != 'quit':
    age = input('Please enter your age, enter quit to exit ')

    if age != 'quit':
        if int(age)> 0 and int(age) < 3:
            print('your ticket is free')
        elif int(age) >= 3 and int(age) <= 12:
            print('your ticket is $10')
        elif int(age) > 12:
            print('your ticket is $15')
        else:
            print('please enter a relevant age')

"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value.
"""

active = True
age = ""

while active:
    age = input('Please enter your age, enter quit to exit ')
    
    if age == 'quit':
        active = False
    else:
        print(age)
        if int(age)> 0 and int(age) < 3:
            print('your ticket is free')
        elif int(age) >= 3 and int(age) <= 12:
            print('your ticket is $10')
        elif int(age) > 12:
            print('your ticket is $15')
        else:
            print('please enter a relevant age')


prompt_message = "Please enter your age, enter quit to exit "
age = ""

while True:
    age = input(prompt_message)
    if age == 'quit':
        break
    else:
        print(age)
        if int(age)> 0 and int(age) < 3:
            print('your ticket is free')
        elif int(age) >= 3 and int(age) <= 12:
            print('your ticket is $10')
        elif int(age) > 12:
            print('your ticket is $15')
        else:
            print('please enter a relevant age')
    
"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""
sandwich_orders = list()
finished_sandwiches = list()

for i in range(1, 5+1):
    sandwich_orders.append('sandwich_name' + str(i))

while sandwich_orders:
    sandwich_name = sandwich_orders.pop()
    print('I made your', sandwich_name)

    finished_sandwiches.append(sandwich_name)

for sandwich in finished_sandwiches:
    print(sandwich, "was made")

"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""
sandwich_orders = ['tuna', 'pastrami', 'spicy', 'cheesy', 'pastrami', 'pastrami']
print('The deli has ran out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = sandwich_orders

for sandwich in finished_sandwiches:
    print(sandwich)

"""
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
"""

responses = dict()
name_message = "What is your name? "
favourite_location_message = "If you could visit one place in the world, what is your dream location? "
poll_message = "Do you want to let another person poll? "

polling_active = True
while polling_active:
    name = input(name_message)
    response_favourite_location = input(favourite_location_message)
    response_poll = input(poll_message)

    responses[name] = response_favourite_location
    if response_poll == 'no':
        polling_active = False

for name, location in responses.items():
    print(name + '\'s favourite place is', location)


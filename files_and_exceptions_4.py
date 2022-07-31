"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""
prompt_message = 'Please enter your name: '
quit_message = 'Please enter yes to continue, no to quit: '

while True:
    username = input(prompt_message)
    if username:
        print('Welcome ' + username.title() + '!')
        with open('guest_book.txt', 'a') as file:
            file.write(username.title() + ' visted\n')

    quit = input(quit_message)
    if quit == 'no':
        break
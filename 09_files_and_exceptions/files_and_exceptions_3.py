"""
'w' : write
'a' : add content to a file, added to end of file
write(): write to file
"""

"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

username = input('Please enter your name: ')
with open('guest.txt', 'w') as file:
    file.write(username.title() + '\n')

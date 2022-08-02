"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

message = 'Why do you like programming? '
quit_message = 'Would you like to continue? Please enter yes to continue, no to quit: '
while True:
    reason = input(message)
    if reason:
        with open('reasons_to_like_programming.txt', 'a') as file:
            file.write(reason + '\n')
    quit = input(quit_message)
    if quit == 'yes':
        continue
    elif quit == 'no':
        break
    else:
        break
"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary.
"""
rivers_dict = dict()
countries = ['singapore', 'malaysia', 'india']
for i in range(0, len(countries)):
    rivers_dict['river_' + str(i)] = countries[i]

for river, country in rivers_dict.items():
    print(f'the name of the river is {river} and it is located in {country}')

"""
6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""
people_for_poll = list()
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for k in favorite_languages.keys():
    people_for_poll.append(k)

people_for_poll.append('bob')
for people in people_for_poll:
    if people in list(favorite_languages.keys()):
        print('thank you for your response!')
    else:
        print('please help us take the poll')
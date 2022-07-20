"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""
person_dict = dict()
person_dict['first_name'] = 'Bob'
person_dict['last_name'] = 'Arum'
person_dict['age'] = 65
person_dict['city'] = 'Las Vegas'

for k,v in person_dict.items():
    print(f'The person\'s {k} is {v}')

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program
"""
favourite_numbers = dict()
for i in range(1, 5+1):
    name = "favourite_number_name_" + str(i)
    favourite_numbers[name] = i

for name, favourite_number in favourite_numbers.items():
    print(f'The person\'s name is {name} and their favourite number is {favourite_number}')

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""
programming_glossary = dict()
programming_glossary['if'] = "for conditions"
programming_glossary['for'] = 'for repeating codes'
programming_glossary['in'] = 'for checking if something exists in a string,list etc.'
programming_glossary['print'] = 'to output something'
programming_glossary['tuple'] = 'immutable data structure'

for k,v in programming_glossary.items():
    print('The meaning of', k, 'is:\n', v)
"""
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
"""

from collections import OrderedDict

glossary = OrderedDict()
glossary['if'] = 'for testing conditions'
glossary['for'] = 'for looping'
glossary['in'] = 'for testing item in a data structure'

for k,v in glossary.items():
    print(k +": " + v)

"""
9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint
class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        rand_number = randint(1, self.sides)
        print(rand_number)

six_sided_die = Die()
for i in range(10):
    print('rolling six sided die', six_sided_die.roll_die())

ten_sided_die = Die(sides=10)
twenty_sided_die = Die(sides=20)
for i in range(10):
    print('rolling ten sided die', ten_sided_die.roll_die())

for i in range(10):
    print('rolling twenty sided die', twenty_sided_die.roll_die())


"""
9-15. Python Module of the Week: One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
http://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, or explore the documentation of
the collections and random modules.
"""

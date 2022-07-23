"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""
def make_shirt(size, text):
    print('The size of the T-shirt is ' + str(size) + ' and ' + text)

# positional argument
make_shirt(20, 'the T-shirt is nice')
# keyword arguments
make_shirt(size = 20, text = 'the Tshirt is nice')

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""
def make_shirt(size='large', message = 'I love Python'):
    print('The size of the T-shirt is ' + size + ' and ' + message)

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='I love the T-shirt')

"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country
"""

def describe_city(city, country = 'Singapore'):
    print(city + " is in " + country)

describe_city(city='Singapore')
describe_city(city='Las Vegas', country='USA')
describe_city(city='Boston', country='USA')

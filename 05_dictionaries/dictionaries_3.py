"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""
person_dict = dict()
person_dict['first_name'] = 'Bob'
person_dict['last_name'] = 'Arum'
person_dict['age'] = 65
person_dict['city'] = 'Las Vegas'

person_dict_1 = dict()
person_dict_1['first_name'] = 'Any'
person_dict_1['last_name'] = 'Lee'
person_dict_1['age'] = 40
person_dict_1['city'] = 'California'

person_dict_2 = dict()
person_dict_2['first_name'] = 'Tyler'
person_dict_2['last_name'] = 'Huang'
person_dict_2['age'] = 19
person_dict_2['city'] = 'Ho Chi Minh'

people = list()
people.append(person_dict)
people.append(person_dict_1)
people.append(person_dict_2)

for person in people:
    for k,v in person.items():
        print('The person\'s', k, 'is', v)


"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""

pet_type = ['cat', 'dog', 'hamster']
pet_owner_name = ['bob', 'any', 'tyler']

koby = dict()
melody = dict()
hailey = dict()

pets = list()

pet_name = [koby, melody, hailey]
for count, name in enumerate(pet_name):
    name['pet_type'] = pet_type[count]
    name['pet_owner_name'] = pet_owner_name[count]
    pets.append(name)

print(pets)
for pet in pets:
    print('The pet is a', pet['pet_type'], "and its owner\'s name is", pet['pet_owner_name'].title())

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""
favourite_places = dict()
list_favourite_places = list()

for i in range(1, 9+1, 3):
    list_favourite_places.append(['favourite_place_' + str(i), 'favourite_place_' + str(i+1), 'favourite_place_' + str(i+2)])

print(list_favourite_places)

for n, list_places in enumerate(list_favourite_places):
    favourite_places['name_' + str(n)] = list_places

print(favourite_places)

for name, list_places in favourite_places.items():
    print(name + '\'s favourite places are:')
    print(list_places)

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.

6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program
"""
favourite_numbers = dict()
list_favourite_numbers = list()

for y in range(1, 10+1, 2):
    list_favourite_numbers.append([y, y+1])

print(list_favourite_numbers)

for n, number_list in enumerate(list_favourite_numbers):
    favourite_numbers['name_' + str(n)] = number_list

print(favourite_numbers)

for name, number_list in favourite_numbers.items():
    print(name + '\'s favourite numbers are:')
    print(number_list)

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""

cities = dict()
for i in range(1, 3+1):
    cities_info = dict()
    cities_info['country'] = 'country_' + str(i)
    cities_info['approximate_population'] = i * 100000
    cities_info['fact'] = 'fact_' + str(i)
    cities['city_name_' + str(i)] = cities_info

print(cities)

for name, city_info in cities.items():
    print('The name of the city is', name, 'and the city is from', city_info['country'], 'with an approximate population of', city_info['approximate_population'])
    print('One fact about the city is', city_info['fact'])

"""
6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs from this chapter, 
and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.
"""
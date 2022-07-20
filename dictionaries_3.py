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
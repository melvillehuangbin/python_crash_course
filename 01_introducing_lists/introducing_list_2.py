"""
3-4: list of people to invite to dinner
"""
dinner_list = ['melville', 'neville', 'batrisyia']
for person in dinner_list:
    print(f"Hi {person}! You are invited to dinner")

"""
3-5: name of guest that can't make it
replace name of guest who cant't make it with new person I am inviting
second set of invitation message of each person in list
"""
new_dinner_list = ['melville', 'neville', 'batrisyia', 'yolanda']
person_not_coming = new_dinner_list[1]
new_dinner_list[1] = 'ying qian'
for person in new_dinner_list:
    print("Hi", person.title() + ",", "you are invited to the dinner!")
print(person_not_coming.title(), "is not coming.")


"""
3-6: extension of 3-4 and 3-5
insert at beggining of list
insert at middle of list
append at end of list
print new message one for each person in list
"""
new_dinner_list.insert(0, 'brandon')
middle = int(round(len(new_dinner_list), 1))
new_dinner_list.insert(middle, 'darren')
new_dinner_list.append('eugene')
for person in new_dinner_list:
    print("Hi", person.title() + ",", "you are invited to dinner")
print('A bigger table is found with 3 new friends invited')


"""
3-7: pop, del
only two person left for dinner, pop until only two names remaining in list
print message to each of two person in list, letting them know they are still invited
del to remove last 2 names in list, returning an empty list
"""
new_dinner_list.pop()
new_dinner_list.pop()
new_dinner_list.pop()
new_dinner_list.pop()
new_dinner_list.pop()

for person in new_dinner_list:
    print("Hi", person.title() + ",", "you are invited to dinner")

del new_dinner_list[1]
del new_dinner_list[0]

print(new_dinner_list)

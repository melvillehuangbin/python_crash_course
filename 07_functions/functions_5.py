"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time
"""

def make_sandwich(*sandwich_items):
    print('The items ordered for the sandwich are: ')
    for item in sandwich_items:
        print('- ' + item)

make_sandwich('sandwich_item_1', 'sandwich_item_2')
make_sandwich('sandwich_item_2', 'sandwich_item_3', 'sandwich_item_4')
make_sandwich('sandwich_item_2', 'sandwich_item_3', 'sandwich_item_4', 'sandwich_item_5')


"""
8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""
def build_profile(first, last, **user_info):
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user = build_profile('Bart', 'Simpson', personality = 'cool', appearance = 'funky', color = 'yellow')
print(user)

"""
8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""
def make_car(manufacturer, model_name, **other_info):
    car_info = dict()
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    for k,v in other_info.items():
        car_info[k] = v
    return car_info

car = make_car('Toyota', 'Wish', color = 'black', tow_package = True)
print(car)
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant\'s name is ' + self.restaurant_name.title() + ' and it sells ' + self.cuisine_type.title() + ' cuisine')
    
    def open_restaurant(self):
        print('The restaurant is opened!')

class User():

    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_restaurant(self):
        print('Summary of user\'s information: ')
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        for k, v in self.user_info.items():
            print(k.title() + ": " + v)

    def greet_user(self):
        print('Hi ' + self.first_name + '! Welcome!')


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class AdminNew(User):

    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])


"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant\'s name is ' + self.restaurant_name.title() + ' and it sells ' + self.cuisine_type.title() + ' cuisine')
    
    def open_restaurant(self):
        print('The restaurant is opened!')

class IceCreamStand(Restaurant):

    def __init__(self, flavors, restaurant_name, cuisine_type):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

flavors = ['vanilla', 'mango', 'coconut']
ice_cream_stand = IceCreamStand(flavors, 'uncle ice cream', 'desert')
ice_cream_stand.display_flavors()


"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""

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

class Admin(User):

    def __init__(self, privileges, first_name, last_name, **user_info):
        self.privileges = privileges
        super().__init__(first_name, last_name, **user_info)

    def show_privileges(self):
        for privilege in privileges:
            print(privilege)

privileges = ['can add post', 'can delete post', 'can ban user']
admin = Admin(privileges, 'Bart', 'Simpson', username = 'bart_simpson', password = 'simpson1234')
admin.show_privileges()

"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges
"""
class Privileges():

    def __init__(self, privileges = privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in privileges:
            print(privilege)

class AdminNew(User):

    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()

admin_new = AdminNew('Bart', 'Simpson', username = 'username')
admin_new.privileges.show_privileges()



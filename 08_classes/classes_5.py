"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly
"""
from classes_modules import Restaurant, User, Privileges, AdminNew

restaurant = Restaurant('Macdonalds', 'Fast Food')
restaurant.describe_restaurant()

"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

privileges = ['can add post', 'can delete post', 'can ban user']
admin_instance = AdminNew('Bart', 'Simpson', user_name = 'bart', password = 'simpson')
admin_instance.privileges.show_privileges()



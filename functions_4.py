"""
8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
"""
magician_names = list()
for i in range(1, 5+1):
    magician_names.append('magician_name_' + str(i))

def show_magicians(magician_name_list):
    for name in magician_name_list:
        print(name)

show_magicians(magician_names)

"""
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
"""
def make_great(magician_name_list):
    new_magician_name_list = list()
    for name in magician_name_list:
         new_name = 'Great_' + name
         new_magician_name_list.append(new_name)
    return new_magician_name_list

def show_magicians(magician_name_list):
    new_magician_name_list = make_great(magician_name_list)
    for name in new_magician_name_list:
        print(name)

show_magicians(magician_names)


"""
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.
"""
new_magicians_names = make_great(magician_names[:])
show_magicians(magician_names)
show_magicians(new_magicians_names)
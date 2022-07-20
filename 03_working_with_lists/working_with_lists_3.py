"""
4-10: slices, print first three items in list
print three items from middle of list
print last three items from list
"""
hundred_thousand_list = [number for number in range(1, 100000+1)]
print("the first three items in the list are:", hundred_thousand_list[0:3])
middle = int(len(hundred_thousand_list)/2 - 1)
print("Three items from the middle of the list are:",
      hundred_thousand_list[middle:middle+3])
print("The last three items in the list are:", hundred_thousand_list[-3:])

"""
4-11: make copy of list of pizzas, call it friend_pizzas
"""
pizza_original = ['haiwaiin', 'pepperoni', 'bbq']
friend_pizzas = pizza_original[:]
pizza_original.append('cheesy')
friend_pizzas.append('spicy')
print("My favourite pizzas are:")
for pizza in pizza_original:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

"""
4-12: print foods in list
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

for food in my_foods:
    print(food)
for food in friend_foods:
    print(food)

"""
4-13: five simple foods store in typle
"""
five_foods = ('rice', 'noodle', 'fruit', 'meat', 'vegetable')
for food in five_foods:
    print(food)

five_foods = ('fried rice', 'fried noodle', 'fruit','meat', 'vegetable')
for food in five_foods:
    print(food)

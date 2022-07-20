"""
4-3: count to twenty using for loop
"""
for i in range(1, 20 + 1):
    print(i)

"""
4-4: list of numbers from one to one million
"""
one_million_numbers_list = [value for value in range(1, 1000000 + 1)]
print(one_million_numbers_list)

"""
4-5: summing a million, list of numbers from one to one million
"""
million_list = [number for number in range(1, 1000000 + 1)]
print(min(million_list), max(million_list), sum(million_list))

""""
4-6: make a list of odd numbers from 1 to 20
"""
list_odd_numbers = [number for number in range(1, 20+1, 2)]
print(list_odd_numbers)

"""
4-7: make list of multiples of 3 from 3 to 30
"""
multiples_of_three_list = [number*3 for number in range(1, 10+1)]
for number in multiples_of_three_list:
    print(number)

"""
4-8: cubes, make a list of first 10 cubes, covers list comprehension as well
"""
list_cubes = list()
for i in range(1, 10+1):
    list_cubes.append(i**2)
print(list_cubes)

"""
4-9: first 10 cubes list comprehension
"""
list_cubes = [number**2 for number in range(1, 10+1)]
for cube in list_cubes:
    print(cube)

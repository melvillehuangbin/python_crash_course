"""
8-15. Printing Models: Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions.
"""
from printing_functions import print_models
unprinted_designs = [('unprinted_design_' + str(i)) for i in range(1,5+1)]
completed_designs = []
print_models(unprinted_designs, completed_designs)
print('The completed designs:', completed_designs)

"""
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.
"""
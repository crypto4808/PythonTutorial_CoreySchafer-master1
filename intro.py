#import as a smaller name so you don't have to type 'my_modules' each time
# import my_modules
# #from  my_module import find_index
# courses = ['history', 'math' , 'physics' , 'compsci' ]
# index = my_modules.find_index(courses,'math')#
# print(index)


#Use shorthand for my_modules so you don't have to type it out all the time
# import my_modules as mm
# courses = ['history', 'math' , 'physics' , 'compsci' ]
# index = mm.find_index(courses,'math')
# print(index)


# #import the function itself
# from my_modules import find_index
# courses = ['history', 'math' , 'physics' , 'compsci' ]
# index = find_index(courses,'math')
# print(index)

# #import the function itself
# #access the test variable from my_modules
# from my_modules import find_index,test
# courses = ['history', 'math' , 'physics' , 'compsci' ]
# index = find_index(courses,'math')
# print(index)
# print(test)



# #import the function itself
# #access the test variable from my_modules
# from my_modules import find_index as fi, test
# courses = ['history', 'math' , 'physics' , 'compsci' ]
# index = fi(courses,'math')
# print(index)
# print(test)


#import everything though it's frowned upon
#Reason is if something goes wrong with find_index
#it's virtually impossible to find which module it was imported from
#access the test variable from my_modules
# from my_modules import *
# courses = ['history', 'math' , 'physics' , 'compsci' ]
# index = find_index(courses,'math')
# print(index)


#how does python know where is the module?
#py checks multiple locations for this modules
from my_modules import find_index, test
import sys
courses = ['history', 'math' , 'physics' , 'compsci' ]
index = find_index(courses,'math')
print(index)
print(sys.path)

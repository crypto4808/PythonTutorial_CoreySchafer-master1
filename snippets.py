

# Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
#
# print(list_1)
# print(list_2)


# Immutable
#using paranthesis() instead of square braces
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' #type error because it's imutable
#
# print(tuple_1)
# print(tuple_2)

# Sets
#we're using curly braces
cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

#order of printing changes from execution to execution
#sets don't care about order
#set is used only to remove duplicate values
#sets are used to do a membership test


print(cs_courses)

print('Math' in cs_courses)

#What courses do these sets have in common
cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))

#print all the courses or a union

print(cs_courses.union(art_courses))



# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

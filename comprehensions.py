#Lesson5:-List Comprenehsions 05/16/18
#https://www.youtube.com/watch?v=3dt4OGnU5sM
#Easy to write and read lists in this format


nums = [1,2,3,4,5,5,7,8,9,10]

#i want 'n' for each 'n' in nums


my_list = []
my_list_squares = []

# for n in nums:
#     my_list.append(n)
# print(my_list)

#LIST COMPREHENSION
#This is better to comprehend than lines #13 to #15
# my_list = [n for n in nums]
# print(my_list)

#
# for n in nums:
#     my_list_squares.append(n*n)
# print(my_list)

# my_list_squares = [n*n for n in nums]
# print(my_list_squares)

#Using a map + lambda
#Convert the maps and lambdas into list comprehesions for better readability
#map and lambda did't print out
# my_list = map(lambda n: n*n, nums)
# print my_list


#I want 'n' for each 'n' in nums if 'n' is even

# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list) #moving print statemtent around prints different results
#
# #Exact same result as above but with better readability
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# #USING a filder + lambda
#Upon Run it results in -> <filter object at 0x1040b8cf8>

# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)

#I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num)) #This is a tuple
# print(my_list)


#list comprehension format
#
# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)


#Dictionary comprehension
names = ['Bruce', 'Clark', 'Peter',  'Logan','Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# I want a dict{'name': 'hero')} for each name,hero in zip(name,heros)
#dictionary with name as key and hero as values
# store into a zip() which is a tuples
my_dict={}
#
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

#Dictionary Comprenehsion
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)
#
#
# #Exclude Spiderman
# my_dict = {name: hero for name, hero in zip(names, heros) if name!= 'Peter'}
# print(my_dict)


#SET COMPREHENSIONS : A set is like a list but with unique values

# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set) #only prints unique values


#Convert to set COMPREHENSIONS
# my_set = {n for n in nums}
# print(my_set)


#GENERATOR EXPRESSIONS
#Generators are a lot different from dictionaries/sets/my_list_squares
#Included in this tutorial because a genereator is very similar to a list COMPREHENSIONS

#I want to yield 'n*n' for each 'n' in nums

nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print(i)


#USING GENERATOR COMPREHENSION
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)

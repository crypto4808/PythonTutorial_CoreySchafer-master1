#Lesson#4 ->conditionals and booleans
#Youtube Link -> https://www.youtube.com/watch?v=DZwmZ8Usvnk

if True:
    print('conditional was True')



language  = 'Python'

language1  = 'Python'


#Notice that autoindent feature was On for the print statemtn
#without spaces before print/if/else py3 throws an error message
if language == 'Python':
    print('Language is Python')
else:
    print('No match')



#set language to Java to fail the test case
language = 'Java'

if language == 'Python':
    print('Language is Python')
else:
    print('No match')

#elif to test both possibilities or the SWITCH case
#there is no explicit switch case in py
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')


#Exploring boolean cases
#and or not

user = 'Admin'
logged_in = True

if (user == 'Admin') and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


user = 'Admin'
logged_in = False

if (user == 'Admin') and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


if (user == 'Admin') or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

#double negative or do the operation if the boolean is false
if not logged_in:
    print('Please log in')
else:
    print('Welcome')

#Compare two lists
a = [1,2,3]
b = [1,2,3]
print(a == b) #returns true
print(a is b) #returns false because it compared ids in memory
print(id(a))
print(id(b))
b=a #now the ids are the same and should print true for below comparison
print(a is b)

#the above print statement is same as
print(id(a) ==  id(b))


#false, none, zero, any empty seq, any empty mapping
#
condition = False
if condition:
    print('Evaluate to True')
else:
    print('Evaluated to False')

#none actually evaluates to a false
condition = None
if condition:
    print('Evaluate to True')
else:
    print('Evaluated to False')


#none actually evaluates to a false
condition = 10
if condition:
    print('Evaluate to True')
else:
    print('Evaluated to False')



#empty string''/list()/tuple[]/dictionary{} also evaluate to false
condition = []
if condition:
    print('Evaluate to True')
else:
    print('Evaluated to False')


condition = 'Test'
if condition:
    print('Evaluate to True')
else:
    print('Evaluated to False')

#Sandip 5May2018
#Lesson1: Strings and working with Textual Data
#Youtube link->https://www.youtube.com/watch?v=k9TUPpGqYTo&index=1&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

print('hello world-1')

message_2 ="Hello World-2"
print(message_2)

message_3= 'Boby\'s world'
print(message_3)

message_4= "Boby's World"
print(message_4)

print('The length=',len(message_4))
print('1st letter=',(message_4[0]))
print('10th letter=',(message_4[10]))
print('1st to 5th letters=',(message_4[0:6]))
print('6th letter to end=',(message_4[6:]))

#method is a function that belongs to an object

print(message_2.lower())
print(message_2.count('l'))
print(message_2.count('World'))
print(message_2.count('Universe'))

message_2.replace('World','Universe') #This will not replace string
print(message_2)

new_message_2 = message_2.replace('World','Universe')
print(new_message_2) #this will replace the string


greeting = 'Hello'
name = 'Michael'

message_6 = greeting + ',' + name + '. Welcome!'
print(message_6)

#the above is too complicated so we use a formatted string by
#replacing with curly braces {} and use a .format
message_7 = '{}, {}. Welcome!'.format(greeting,name)
print(message_7)


 #fstring recently released but not many are using it though
 #makes string formatting as easy as possible
#Doesn't run on my python
 #message_8 = f'{greeting}, {name}. Welcome!'
 #print(message_8)


print(dir(name)) #shows all attributes
print(help(str.lower))

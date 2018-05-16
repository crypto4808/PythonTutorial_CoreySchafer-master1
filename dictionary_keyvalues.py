
#Dictionary and key values
student = {'name':'John','age':25,'courses':['Math','CompSci']}
print(student)



#test
#test2

#to access the student variables via keys
print(student['name'])
print(student['courses'])
print(student['age'])


student = {'1':'John','age':25,'courses':['Math','CompSci']}
# print(student)

#keys can be integers or strings
print(student['1'])


student = {'name':'John','age':25,'courses':['Math','CompSci']}
#print(student['phone']) #throws an error message since key doesn't exist

#using the get method there is no error message when key doesn't exist
#best practice to use the get method that can handle exceptions
print(student.get('phone')) #returns a none

student['phone'] = '555-5555'
student['name'] ='Jane'

print(student.get('phone','Not found'))
print(student)

#better way to update the key and value pairs in dictionary
student.update({'name':'Jessica','age': 46 ,'phone':'555-5555'})
print(student)


#delete a key-value pair
del student['age']
print(student)

#delete key-value pairs using the pop method
student = {'name':'John','age':25,'courses':['Math','CompSci']}
print(student)
#pop a key and also capture the popped value and print it
age = student.pop('age')
print(student)
print(age)

#print the number of keys in the dictionary
print(len(student))
print(student.keys()) #see all the keys of the dictionary
print(student.values()) #see all the values in the dictionary
print(student.items()) #all the items in the dictionary

student = {'name':'John','age':25,'courses':['Math','CompSci']}

#looping this way will only print the keys
for key in student:
    print(key)

#looping this way will print the key and values
for key,value in student.items():
    print(key,value)

#Lesson7: Sorting lists/strings
#https://www.youtube.com/watch?v=D3JvDWO-BY4&t=3s

#Task is to sort a few  different data types
li = [9,1,8,2,7,3,6,4,5]

#The sorted function returns a new variable
s_li = sorted(li)
# print(sorted.__doc__)
# print(dir(sorted))
print('Sorted Variable:\t',s_li)
print('Original List:\t',li)


#sorting without creating a new Variable
#The sort() method modifies the list in place
#The sort() method doesn't return a list
# li.sort() #This sorts the original list
print('Original List:\t',li)


#Task is to sort a few  different data types
li = [9,1,8,2,7,3,6,4,5]

# #The in decending order
s_li = sorted(li, reverse = True)
print('Sorted Variable:\t',s_li)


li.sort(reverse = True)
# print(sorted.__doc__)
print('Original List:\t',li)

#The sorted() function is more flexible than the sort() method
#The sorted() function can accept any data types
#The sort() method can only accept a list[]


#For example if we have a tuple90

tup = (9,1,8,2,7,3,6,4,5)

# tup.sort() #This gives an error since the sort method can only accept a list[]

s_tup = sorted(tup )
print('Tuple\t',s_tup)


#Dictionary datatype with the sorted() function
di = {'name':'SandMan','job':'engineer','age': None,'os': 'Mac'}
s_di = sorted(di) #this will only sort the keys
print('Dict\t',s_di)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs) #sort in terms of absolute value
print(s_li)
# print()

class Employee():
    def __init__(self,name,age,salary):
        self.name= name
        self.age=age
        self.salary = salary

    def __rep__(self):
        return'

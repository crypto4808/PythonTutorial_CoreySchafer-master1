#lists and tuples are meant to work with sequential data
#lists- like the name implies it allows us to work with a list of values
#lets say we want a list of courses

courses = ['History','Math','Physics','CompSci']
print('The list of courses is ', courses)

#how many values in the list
print('The number of courses is',len(courses))

print(courses[0])
print('The last item is ->',courses[len(courses)-1])
print('Another way to print the last item ->',courses[-1])

#print('Ivalid index of couses ->',courses[6])

print(courses[0:2])

print(courses[:2])
print(courses[2:])

#add item to the end of the lists
courses.append('Art')
print(courses)

#insert at an index location
courses.insert(0,'Chem')
print(courses)


#courses_2= 'mech','tronix']

#courses.insert(0, courses_2)
print(courses)

courses_3 =['ofc','dld']
courses.extend(courses_3)
print(courses)

#how to remove values from a list

courses.remove('Math')
print(courses)

#by default removes the last value
courses.pop()
print(courses)

#assign the popped value to a variable
popped = courses.pop()

print(popped)
print(courses)

#reverse the list
courses.reverse()
print(courses)

#print in ascending order

courses.sort()
print(courses)

nums =[1,5,2,4,3]
nums.sort()
print(nums)

#print in decending order
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

#Sorting the list without altering the original list
#sorted version of the courses list without affecting the original

courses = ['History','Math','Physics','CompSci']

sorted_courses =sorted(courses)
#print(courses)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))
#print(courses.index('Art')) #art is not in the lists

print('Art' in courses)
print('Math' in courses)

for item in courses:
    print(item)

#prints the index and the course
    for course in enumerate(courses):
        print(course)

    for index, course in enumerate(courses):
        print('Index/course',index, course)

#prints the index and the course with a starting index specified

        for course in enumerate(courses,start =2):
            print(course)



#Convert the list into strings comma separated
courses = ['History','Math','Physics','CompSci']

course_str = ', '.join(courses)
print(course_str)


course_str = ' - '.join(courses)
print(course_str)

#split the string that we just created

new_list =course_str.split(' - ')
print(new_list)

#courses.sort() #Doesn't work

#tuples sets are unordered sets of values with no duplicates

#tuples are like lists but can't be modified or immutable

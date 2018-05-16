# def hello_func():
#     pass
#
#
# print(hello_func())

#
# def hello_func():
#     print('Hello Function!')

#hello_func()

# print('Hello Function!')
# print('Hello Function!')
# print('Hello Function!')
# print('Hello Function!')



# hello_func()
# hello_func()
# hello_func()
# hello_func()



#functions help us operate on the data and print the results
#when you execute a function, it'll be equal to a value

# def hello_func():
#     return 'Hello Function!'

#Now the function return can use the string methods
# print(hello_func().upper())
# print(len('Test'))


#pass an argument to the function (greeting,name and default return)
# def hello_func(greeting,name = "you"):
#     return '{} , {} Function.' .format(greeting, name)
#
# print(hello_func('Hi')) #uses the default value of the name arg

# print(hello_func('Hi' , name = 'Corey')) #here we pass an actual value for the name arg

#args and key for the args or positional
#args and kwargs are the norm or convention
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# student_info('Math','Art', name ='John', age =22 )

# cou nt_info(*courses, **info) #This prints out the *args/**kwargs


#Below code from the following link
#https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Functions/snippets.txt
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))

print(days_in_month(2017,2))

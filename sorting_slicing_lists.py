#slicing on lists and strings

#slicing= extracting certain elements from your list or strings
my_list = [0,1,2,3,4,5,6,7,8,9]
#pos index    0,1,2,3,4,5,6,7,8,9
#neg index    -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,

# print(my_list)

# print(my_list[9])
# print(my_list[-1])
# print(my_list[-10])
#
#
# print(my_list[3:8])
#
# print(my_list[-7:-2])
#
# print(my_list[1:-2])
#
# print(my_list[:-1]) #prints index from 0 onwards to -1
# print(my_list[2:-1])
#
#prints 2 to 8 but print ever other value
# print(my_list[2:-1:2]) #STEP SIZE =2
#
#print 2 to 8 but negative step doesn't work like that
# print(my_list[2:-1:-1])#STEP SIZE = -1

#print  8 to 2 but negative step works
print(my_list[-1:2:-1])#STEP SIZE = -1


#print  8 to 2 but negative step works
print(my_list[-2:1:-1])#STEP SIZE = -1

#PRINT LIST IN REVERSE
print(my_list[::-1])


#EXAMPLE OF A URL
sample_url = 'http://sandms.com'
print(sample_url)

#Get top level domain
print('Top level domain:',sample_url[-4:])

#Print the url without the http://
print(sample_url[7:])

#Print URL without the http:// or the top level domain
print(sample_url[7:-4])

from datetime import datetime
import os
f = open('test.txt')

#open for read only
f = open('test.txt','r')
# print(f.name)
# print('The mode of file:',f.mode)
#if you don't close the file then you'll run into errors
#max file size will be exceeded
f.close()


# #open for write
# f = open('test.txt','w')
#
# #open for appen
# f = open('test.txt','a')
#
#
# #open for read/write
# f = open('test.txt','a')


#this will automatically close the file#
#handles file exceptions
#we have access to the file mode even after it's closed
with open('test.txt','r') as f:
#    f_contents = f.read() #okay for small files
    #f_contents = f.readlines() #reads all lines
    f_contents = f.readline() #reads only the first line
    # print(f_contents, end ='') #end removes the newline


#if you repeat the readline it prints the next line
    f_contents = f.readline() #reads only the first line
    # print(f_contents,end ='')  #end removes the newline


#if you repeat the readline it prints the next line
    f_contents = f.readline() #reads only the first line
    # print(f_contents) # #end removes the newline


#how to iterate over all the lines in the file and print them out
#this is very efficient since it doesn't read the entire file at onceself.
#if only fetches one line at a timeself
#this is enough for most purposes of file handling/manipulation
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line,end='')


#using f.read()
# with open('test.txt', 'r') as f:
#     # f_contents = f.read() #prints the whole file
#     f_contents = f.read(100) #prints the first 100 characters
#     print(f_contents, end ='') #end removes the newline
#
#
#     f_contents = f.read(100) #prints the next 100 characters
#     print(f_contents, end ='') #end removes the newline
#
#     f_contents = f.read(100) #prints the next 100 characters
#     print(f_contents, end ='') #end removes the newline
#
#     f_contents = f.read(100) #does nothing since we reached end of the file
#     print(f_contents, end ='') #end removes the newline



#Instead of hardcoding 100 characters let's use a variable size_to_read

# with open('test.txt', 'r') as f:
#     # f_contents = f.read() #prints the whole file
#     size_to_read = 10
#     f_contents = f.read(size_to_read) #prints size_to_read number of characters
#     while len(f_contents) >0:
#         print(f_contents, end ='*') #end removes the newline
#         print(f.tell()) #tells where we are in the file
#         f_contents = f.read(size_to_read)
with open('test.txt', 'r') as f:
    # f_contents = f.read() #prints the whole file
    size_to_read = 10
    f_contents = f.read(size_to_read) #prints size_to_read number of characters
    print(f_contents, end='')
    # print(f.tell()) #tells where we are in the file

#start with the beginning of the file instead of incrementing the position
    f.seek(0)
    f_contents = f.read(size_to_read) #prints size_to_read number of characters
    print(f_contents, end='')


#WRITE TO A file
# with open('test.txt', 'r') as f: #error writing if in  read mode

# with open('test.txt', 'w') as f: #error writing if in  read mode
#     # f.write('We just wrote this new line', datetime.fromtimestamp(mod_time))
#     f.write('We just wrote this new line')
#
# with open('test.txt', 'a') as f: #error writing if in  read mode
#     # f.write('We just wrote this new line', datetime.fromtimestamp(mod_time))
#     f.write('We just wrote the next line')
#     f.seek(0)
#     f.write('R')

with open('test.txt', 'r') as rf: #open in read mode
    with open('test_copy.txt', 'w') as wf: #open in write mode -nested
        for line in rf:
            wf.write(line)

from datetime import datetime
import datetime
import datetime as dt
import os
# f = open('test.txt')
#
# #open for read only
# f = open('start_finish_times.txt','r')
# print(f.name)
# print('The mode of file:',f.mode)
# # #if you don't close the file then you'll run into errors
# # #max file size will be exceeded
# f.close()
#
#
# # #open for write
# # f = open('test.txt','w')
# #
# # #open for appen
# # f = open('test.txt','a')
# #
# #
# # #open for read/write
# # f = open('test.txt','a')
#
#

#Open and write a small file it's okay do this
#This will print out all the lines in the file
# with open('start_finish_times.txt','r') as f:
#    f_contents = f.read() #okay for small files
#    print(f_contents)

# #this will automatically close the file#
# #handles file exceptions
# #we have access to the file mode even after it's closed
# with open('start_finish_times.txt','r') as f:
    # f_contents = f.readlines() #reads all lines
# #prints the first line
#     f_contents = f.readline() #reads only the first line
#     print(f_contents, end ='') #end removes the newline
#
# #prints the second line
#     f_contents = f.readline() #reads only the first line
#     print(f_contents, end ='') #end removes the newline



#
# #if you repeat the readline it prints the next line
#     f_contents = f.readline() #reads only the first line
#     # print(f_contents,end ='')  #end removes the newline
#
#
# #if you repeat the readline it prints the next line
#     f_contents = f.readline() #reads only the first line
#     # print(f_contents) # #end removes the newline
#
#
# #how to iterate over all the lines in the file and print them out
# #this is very efficient since it doesn't read the entire file at onceself.
# #if only fetches one line at a timeself
# #this is enough for most purposes of file handling/manipulation
#this is great for memory usage purposes
# with open('start_finish_times.txt', 'r') as f:
#     for line in f:
#         print(line,end='')
#
#
# using f.read() to specify the
#number of characters of data to be read

# with open('start_finish_times.txt', 'r') as f:
#     # f_contents = f.read() #prints the whole file
#     f_contents = f.read(200) #prints the first 100 characters
#     print(f_contents, end ='') #end removes the newline
#
# #read will return an empty string
#     f_contents = f.read(10) #prints the next 100 characters
#     print(f_contents, end ='') #end removes the newline

# #     f_contents = f.read(100) #prints the next 100 characters
# #     print(f_contents, end ='') #end removes the newline
# #
# #     f_contents = f.read(100) #does nothing since we reached end of the file
# #     print(f_contents, end ='') #end removes the newline
#
#
#
# #Instead of hardcoding 100 characters let's use a variable size_to_read
#
# with open('start_finish_times.txt', 'r') as f:
#     # f_contents = f.read() #prints the whole file
#     size_to_read = 10
#     f_contents = f.read(size_to_read) #prints size_to_read number of characters
#     while len(f_contents) >0:
#         print(f_contents, end ='*') #end removes the newline
#         print(f.tell()) #tells where we are in the file
#         f_contents = f.read(size_to_read)
# with open('start_finish_times.txt', 'r') as f:
#     # f_contents = f.read() #prints the whole file
#     size_to_read = 10
#     f_contents = f.read(size_to_read) #prints size_to_read number of characters
#     print(f_contents, end='')
#     # print(f.tell()) #tells where we are in the file
#
# #start with the beginning of the file instead of incrementing the position
#     f.seek(0)
#     f_contents = f.read(size_to_read) #prints size_to_read number of characters
#     print(f_contents, end='')
# #
#
# #WRITE TO A file
# #This method creates a new file
# with open('test2.txt', 'w') as f: #error writing if in  read mode
#     f.write('line1\n')
#
#     f.write('linie2')

#
# with open('test.txt', 'w') as f: #error writing if in  read mode
# #     # f.write('We just wrote this new line', datetime.fromtimestamp(mod_time))
# #     f.write('We just wrote this new line')
# #
# with open('test.txt', 'a') as f: #error writing if in  read mode
#     # f.write('We just wrote this new line', datetime.fromtimestamp(mod_time))
#     f.write('We just wrote the next line')
#     f.seek(0)
#     f.write('R')

# with open('start_finish_times.txt', 'r') as rf: #open in read mode
#     with open('SF_copy.txt', 'w') as wf: #open in write mode -nested
#         for line in rf:
#             wf.write(line)


#Open an image file using the same methodology
#We get an error message 'cant decode byte in 0 position'
#So inorder to work with images, we have to ready/write bytes or Binary
#Binary mode is by using 'rb/wb' instead of 'r/w'
# with open('astronaut.jpg', 'rb') as rf: #Read in binary mode
#     with open('astronaut_copy.jpg', 'wb') as wf: #Write in binary mode
#         for line in rf:
#             wf.write(line)

#Do the same  above operation in chunk sizes
with open('astronaut.jpg', 'rb') as rf:
    with open('astronaut_copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


#051518 Calculate laptimes from the racetrack using datetime

#get to

# t1 = '0:3:2'
# t2 = '0:4:58'
# t3 = '0:6:53'
# t4 = '0:8:50'
# t5 = '0:10:46'
# #
# #
# # # print('Lap2 S\F:',t2)
# # # print('Lap3 S\F:',t3)
# # # print('Lap4 S\F:',t4)
# # # print('Lap5 S\F:',t5)
# #
# # FMT = '%H:%M:%S'
# # #
# # lap_1 = datetime.strptime(t2, FMT) -datetime.strptime(t1, FMT)
# # # print('Lap1 S\F:',lap_1)
#
#
#
# # start="09:35:23"
# # end="10:23:00"
# sf_t1 = dt.datetime.strptime(t1, '%H:%M:%S')
# sf_t2 = dt.datetime.strptime(t2, '%H:%M:%S')
# sf_t3 = dt.datetime.strptime(t3, '%H:%M:%S')
# sf_t4 = dt.datetime.strptime(t4, '%H:%M:%S')
# sf_t5 = dt.datetime.strptime(t5, '%H:%M:%S')
#
# lap_1 = (sf_t2 - sf_t1)
# lap_2 = (sf_t3 - sf_t2)
# lap_3 = (sf_t4 - sf_t3)
# lap_4 = (sf_t4 - sf_t3)
#
# # diff.seconds/60
# print(lap_1)
# print(lap_2)
# print(lap_3)
# print(lap_4)
# # print(lap_5)

import csv

# #use a context manager to open the file
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file) #reader method uses a dialect
#     #by default , the reader expects a comma separated format
#
#     next(csv_reader) #This will skip over the first line
#     # print(csv_reader) # this won't work, we need to loop through
#     #
#     for line in csv_reader:
#         print(line) #prints all the CSV lines minus the header
#         # print(line[2]) #index 2 prints all emails
#

#Save the same values in to a new CSV file
#
# #use a context manager to open the file
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file) #reader method uses a dialect
#     #by default , the reader expects a comma separated format
#
# #OPen a new csv file with deliminter set to '-' instead of ';'
#     with open('new_names1.csv','w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')
#
# #for each line in original file, write line to the new file
#         for line in csv_reader:
#             csv_writer.writerow(line)
#
#


# #use TAB as delimiter
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file) #reader method uses a dialect
#     #by default , the reader expects a comma separated format
#
# #OPen a new csv file with deliminter set to tab
#     with open('new_names_tab.csv','w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
# #for each line in original file, write line to the new file
#         for line in csv_reader:
#             csv_writer.writerow(line)



#Now read in the the tab delimited CSV file that we created
#Prints everything as a single line without splitting
# with open('new_names_tab.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file) #reader method uses a dialect
#     #by default , the reader expects a comma separated format
#
#     for line in csv_reader:
#         print(line)


# #Split the lines from the above by specifying the deliminter
# with open('new_names_tab.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t') #This will split the lines
#
#     for line in csv_reader:
#         print(line)


# #Corey prefers working with CSV file io using the dictionary reader/
# #instead of the regular reader method
#
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.DictReader(csv_file) #reader method uses a dialect
#     #by default , the reader expects a comma separated format
#
#
# #Now everything is stored as key/index pair
#     for line in csv_reader:
#         # print(line)
#         print(line['email']) #prints all the emails



#Corey prefers working with CSV file io using the dictionary reader/
#instead of the regular reader method

#
# #

#Advantage of working with dictionary
#For example to Delete the emails

 #use a context manager to open the file
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #reader method uses a dialect
    #by default , the reader expects a comma separated format

#OPen a new csv file with deliminter set to '-' instead of ';'
    with open('new_names_dict_1.csv','w') as new_file:
        fieldnames_ = ['first_name','last_name'] #Delete 'emails'
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames_, delimiter='-')

#To write the header
        csv_writer.writeheader()
#Email line will be deleted
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

#

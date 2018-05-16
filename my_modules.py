#importing modules


print('Imported my_module...')


test = 'Test string'

#to_search= the list to search
#targed = the search
def find_index(to_search,target):
    '''Find the index of a value in a sequencer'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1


    

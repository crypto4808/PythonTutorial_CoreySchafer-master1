#Youtube linkk-> https://www.youtube.com/watch?v=tJxcKyFMTGo
import os

from datetime import datetime
print(os.getcwd())


#change directory to desktop
os.chdir('/Users/admin/Desktop')
print(os.getcwd())

#list the list of directories on the desktop
print(os.listdir())


#create a new folder on the desktop
#method1
os.makedirs('OS_Demo_2/Sub_Dir_1')
os.removedirs('OS_Demo_2/Sub_Dir_1') #removes single directory

#rename files and then list dirs
os.makedirs('test.txt')
os.rename('test.txt','demo.txt')
print(os.listdir())

#display the attributes of the files
print(os.stat('demo.txt'))

print('The size of the file is ', os.stat('demo.txt').st_size)
print('The modification time of the file is ', os.stat('demo.txt').st_mtime)

#get the mod time in human readable format
mod_time = os.stat('demo.txt').st_mtime
print('The modification human readable format is ', datetime.fromtimestamp(mod_time))


#Os walk is a generator that yields a tuple of three values as it walks the directory tree
#each dir it seems it displays the path, the dirs inside the path and also the files

# for dirpath, dirnames, filenames in os.walk('/Users/admin/Desktop'):
# for dirpath, dirnames, filenames in os.walk('/Users/admin/Desktop'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('files:', filenames)
#     print()

#print out the environment variables

print(os.environ.get('HOME'))  #/Users/admin

#let's say you wanted to use the path you got to create a new file/dirs
#how can we combine the path we got from the os.environment

# 'test1.txt'

file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

#but there's always confusion with the slashes using this method1
#to remedy this we use the os.path.join

file_path2= os.path.join(os.environ.get('HOME'),'test.txt2')
print(file_path2)

#file creations will be explored in the following lecture
# with open(file_path, 'w') as f:
#     f.write


print(os.path.basename('tmp/test.txt'))

print(os.path.dirname('tmp/test.txt'))

print(os.path.split('tmp/test.txt'))

#check the existence of the path
print(os.path.exists('tmp/test.txt'))


#Check if dir or file
print(os.path.isdir('tmp/test.txt'))
print(os.path.isfile('tmp/test.txt'))


#split the filename and the extension
#it's a lot easier for file manipulation
print(os.path.splitext('tmp/test.txt'))

print(dir(os.path))

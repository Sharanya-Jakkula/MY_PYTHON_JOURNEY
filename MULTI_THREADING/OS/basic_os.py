import os
# to get the current working directory
cwd=os.getcwd()
print(cwd)

#to change the working directory chdir()
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
current_path() 
os.chdir('../') 
current_path() 

# to create the directory 
directory = "OS_DIRECTORIES"
parent_dir = "MULTI_THREADING/OS/"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print(path)
os.mkdir(path) #--> If already file exists it gives error
print("Directory '% s' created"% directory)
directory = "OS_DIR"
parent_dir = "MULTI_THREADING/OS/"
mode = 0o666 #this provides read and write operations
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created"% directory)



# using the mkdirs()
directory = "Sharanya"
parent_dir = "/MULTI_THREADING/OS/OS_DIRECTORIES"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)
directory = "c"
parent_dir = "/MULTI_THREADING/OS/OS_DIRECTORIES"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print("Directory '% s' created" % directory)

# LISTING OUT PATHS

path = "/"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :") 
print(dir_list) 

# remove
os.remove(path)
os.rmdir(path)
print(os.name)
try:
    filename = 'GFG.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()
except IOError:
  print('Problem reading: ' + filename)

fd = "GFG.txt"

file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

file = os.popen(fd, 'w')
file.write("Hello")
os.close(file)

# rename
fd = "GFG.txt"
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')
os.remove("file_name.txt")
result = os.path.exists("basic_os.py") #giving the name of the file as a parameter.
size = os.path.getsize("filename")
print("Size of the file is", size," bytes.")
print(result)


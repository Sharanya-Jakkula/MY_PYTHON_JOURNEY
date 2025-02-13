#to demonstrate the functionality of OS module
import os
from datetime import datetime
#print(dir(os)) ---> shows the attributes
#print(os.getcwd())  ---> prints the current working directory
os.chdir('/home/rgukt123/Desktop') #--> changing the path
print(os.getcwd())
#os.mkdir('OS-DEMO') ---> make directory
#os.makedirs('Os/SUB-OS') ---> make directory along with sub directories
#print(os.listdir()) --> list of directories
#os.rename('Os','OS-NEW') ---> rename the directory
#os.rmdir('OS-DEMO') ----> REMOVES THE OS-DEMO DIRECTORY
#os.rmdir('SUB-OS')
#print(os.stat('test.txt'))
#print(os.stat('test.txt').st_size)
#print(os.stat('test.txt').st_mtime)
'''mod_time=(os.stat('test.txt').st_mtime)
print(datetime.fromtimestamp(mod_time))
for dirpath,dirnames,filenames in os.walk(os.getcwd()):
    print('Current path : ',dirpath)
    print('Directories : ',dirnames)
    print('files : ',filenames)
    print()'''
#print(os.environ.get('HOME')+'/Desktop')
#print(os.path.join(os.environ.get(('HOME')),'Desktop'))
#print(os.path.exists('/home/rgukt123/Desktop'))
#print(os.path.isdir('/home/rgukt123/Desktop'))
#print(os.path.isfile('/home/rgukt123/Desktop'))
#print(os.path.splitext('/home/rgukt123/Desktop/test.txt'))
print(os.path.split('/home/rgukt123/Desktop/test.txt'))






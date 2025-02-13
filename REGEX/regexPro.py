# to demonstrate the regex expressions along with the file handling
import os
import re
os.chdir('/home/rgukt123/Desktop')
'''pat='[a-zA-Z]*(/d{3}/d{3}/d{4})[a-zA-Z]*'
num='/d{3}/d{3}/d{4}'
print('Current location : ',os.getcwd())
with open('practice.txt','r+') as f:
    st=f.readlines(1)[0]
    print(st)
    print(re.match(num,'9998887777'))'''
txt = "The rain in Spain"
x = re.findall("Spain", txt)
print(x) 
#pat=r'\d{3}\d{3}\d{4}' --> number pattern
#pat1=r'\s' -->to find the patterns 
pat2=r'i[a-z]*'
with open('practice.txt','r+') as f:
    st=f.readlines(1)[0]
    print(st)
    found=re.findall(pat2,st)
    print(found)
    
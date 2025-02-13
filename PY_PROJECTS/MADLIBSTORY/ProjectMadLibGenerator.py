#to generate a story using the input words and also file handling -read story from the file and replace with inputs
import os
import re
os.chdir('/home/rgukt123/Desktop')
with open('story.txt','r+') as f:
    s=f.read()
pat=r'<[a-z]*>'
l=re.findall(pat,s)
#input
for i in (l):
    choice=input(f'Enter the {i} : ')
    s=s.replace(i,choice)
print(s)
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)
# array elements
from array import *
array1 = array('i', [10,20,30,40,50])
for x in array1:
 print(x)
 
#  accessing array elements
print("Accessing array elements")
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

print("inserting the elements")
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
 print(x)

print("deleting the elements")
from array import *
array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
   print(x)

print("searching")
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40)) 

print("updating")
from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)
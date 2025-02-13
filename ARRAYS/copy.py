
# import array as arr
# a = arr.array('i', [1, 2, 3, 4, 5])
# b=a.copy()
# print(b)

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
b=a
print (id(a), id(b))
a[2]=10
print (a,b)

# To create another physical copy of an array, we use another module in Python library, named copy and use deepcopy() function in the module. A deep copy constructs a new compound object and then, recursively inserts copies into it of the objects found in the original
import array,copy
a = arr.array('i', [1, 2, 3, 4, 5])
import copy
b = copy.deepcopy(a)
print (id(a), id(b))
a[2]=10
print (a,b)

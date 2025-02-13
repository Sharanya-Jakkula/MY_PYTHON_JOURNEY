import array as arr
print("for loop")
a = arr.array('d', [1, 2, 3])
for x in a:
   print (x)
# d-float
# while Loop
print("while loop")
l = len(a)
idx =0
while idx<l:
   print (a[idx])
   idx+=1
print("for loop with array index")
import array as arr
a = arr.array('d', [1, 2, 3])
l = len(a)
for x in range(l):
   print (a[x])

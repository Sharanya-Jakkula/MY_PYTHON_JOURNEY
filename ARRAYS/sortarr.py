import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print("array before sorting is ",a)
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i]
         a[i] = a[j]
         a[j] = temp
print ("array after sorting is ",a)

print("using sort() method :")
a = arr.array('i', [10,5,15,4,6,20,9])
b=a.tolist()
b.sort()
a = arr.array('i')
a.fromlist(b)
print (a)

print("using sorted method()")
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print (a)
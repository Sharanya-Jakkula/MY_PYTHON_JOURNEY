import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')#empty array
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print (a, b)

print("Using method")
a = arr.array('i', [10,5,15,4,6,20,9])
b = a.tolist()#array to list
b.reverse()
a = arr.array('i')
a.fromlist(b)#array from list
print(b)
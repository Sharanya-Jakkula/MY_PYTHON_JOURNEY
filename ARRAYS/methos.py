import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
print("actual array : ",a)
# reverse
a.reverse()
print ("reverse",a)

# count
a = arr.array('i', [1, 2, 3, 2, 5, 6, 2, 9])
print(a)
c = a.count(2)
print ("Count of 2:", c)
# index
a = arr.array('i', [1, 2, 3, 2, 5, 6, 2, 9])
c = a.index(2)
print ("index of 2:", c)
# fromlista = arr.array('i', [1, 2, 3, 4, 5])
lst = [6, 7, 8, 9, 10]
c = a.fromlist(lst)
print (a)
# tofile
f = open('list.txt','wb')
arr.array("i", [10, 20, 30, 40, 50]).tofile(f)
f.close()

# fromfile
a = arr.array('i', [1, 2, 3, 4, 5])
f = open("list.txt", "rb")
a.fromfile(f, 5)
print (a)
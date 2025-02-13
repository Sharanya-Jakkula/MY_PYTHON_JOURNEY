import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)

# specific indices
a.insert(1,20)
print (a)
# elements from another sequence
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)


#remove-pass element
a1 = arr.array('i', [1, 2, 1, 4, 2])
a1.remove(2)
print (a1)
# pop-pass index
a1.pop(2)
print (a1)

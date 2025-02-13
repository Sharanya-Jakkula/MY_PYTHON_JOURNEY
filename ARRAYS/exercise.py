# Python program to find the largest number in an array 
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)

# Python program to store all even numbers from an array in another array −
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
b = arr.array('i')
for i in range(len(a)):
   if a[i]%2 == 0:
      b.append(a[i])
print ("Even numbers:", b)

# Python program to find the average of all numbers in a Python array −
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
s = 0
for i in range(len(a)):
   s+=a[i]
avg = s/len(a)
print ("Average:", avg)

# Using sum() function
avg = sum(a)/len(a)
print ("Average:", avg)
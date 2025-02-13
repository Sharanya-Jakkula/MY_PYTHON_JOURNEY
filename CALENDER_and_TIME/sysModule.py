#to demonstrate the functioning of the sys module
import sys
print("PYTHON PATH  : ",sys.path)
sys.exit(0)#--> to exit
a=int(sys.argv[1])
b=int(sys.argv[2])
sum=a+b
print(sum)
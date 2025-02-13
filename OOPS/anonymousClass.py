class myclass:
   def __init__(self):
      self.myvar=10
      return
      
obj = myclass()

print ('class of int', type(int))
print ('class of list', type(list))
print ('class of dict', type(dict))
print ('class of myclass', type(myclass))
print ('class of obj', type(obj))

# newclass=type(name, bases, dict)--> type takes three arguments

# each class in python is an instance of the object class
print("Creating the anonymous classes and the objects : ")
anon=type('', (object, ), {})
obj = anon()
print ("type of obj:", type(obj))
def getA(self):
   return self.a
obj = type('',(object,),{'a':5,'b':6,'c':7,'getA':getA,'getB':lambda self : self.b})()
print (obj.getA(), obj.getB())
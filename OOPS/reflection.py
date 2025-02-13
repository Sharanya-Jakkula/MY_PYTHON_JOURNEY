# reflection refers to the ability to extract information about any object in use. You can get to know the type of object, whether is it a subclass of any other class, what are its attributes, and much more.

print("USING THE TYPE() METHOD : ")
print (type(10))
print (type(2.56))
print (type(2+3j))
print (type("Hello World"))
print (type([1,2,3]))
print (type({1:'one', 2:'two'}))

class test:
   pass
   
obj = test()
print (type(obj))

print("USING isinstance method():")
print (isinstance(10, int))
print (isinstance(2.56, float))
print (isinstance(2+3j, complex))
print (isinstance("Hello World", str))
print (isinstance([1,2,3], tuple))
print (isinstance({1:'one', 2:'two'}, set))
print (isinstance(obj, test))
print (isinstance(int, object))
print (isinstance(str, object))
print (isinstance(test, object))

print("Using issubclass() method  :")
print (issubclass(int, object))
print (issubclass(str, object))
print (issubclass(test, object))

#  A Python function, which performs a certain process, is a callable object
print("Using the callable() function :")
print (callable("Hello"))
print (callable(abs))
print (callable(list.clear([1,2])))
print (callable(test))

# A class instance is callable if it has a __call__() method
class test:
   def __init__(self):
       self.name = "Manav"
   def __call__(self):
      print ("Hello")
      
obj = test()
obj()
print ("obj is callable?", callable(obj))

print("Using getattr() method : ")
print (getattr(obj, "name"))

print("Using setattr() method : ")
setattr(obj, "age", 20)
setattr(obj, "name", "Madhav")
print (obj.name, obj.age)

print("Using the hasattr() method : ")
print (hasattr(obj, "age"))
print (hasattr(obj, "name"))

# The dir() Function

# If this built-in function is called without an argument, return the names in the current scope
print("the dir() function : ")
print("For Integer class : ")
print ("dir(int):", dir(int))
print("For dict class : ")
print ("dir(dict):", dir(dict))
print("For object of a class  : ")
print ("dir(obj):", dir(obj))
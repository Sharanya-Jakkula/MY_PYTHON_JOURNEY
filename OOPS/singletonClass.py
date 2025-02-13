# A singleton class is a class in which only one object can be created. This helps in optimizing memory usage when you perform some heavy operation, like creating a database connection.
class SingletonClass:
   _instance = None#main
   
   def __new__(cls):
      if cls._instance is None:
         print('Creating the object')
         cls._instance = super(SingletonClass, cls).__new__(cls)
      return cls._instance
      
obj1 = SingletonClass()
print(obj1)

obj2 = SingletonClass()
print(obj2)

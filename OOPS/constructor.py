# class Employee:
#    'Common base class for all employees'
#    def __init__(self):
#       self.name = "Bhavana"
#       self.age = 24

# e1 = Employee()
# print ("Name: {}".format(e1.name))
# print ("age: {}".format(e1.age))

print("parametrised constructor")
class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

print("Assigning the default parameters")
class Employee:
   'Common base class for all employees'
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age

e1 = Employee()
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

print("instance methods")
class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

e1 = Employee()
e2 = Employee("Bharat", 25)

e1.displayEmployee()
e2.displayEmployee()

print("add and delete methods")
e1.salary = 7000 # Add a 'salary' attribute.
e1.name = 'xyz' # Modify 'name' attribute.
del e1.salary # Delete 'salary' attribute.
print (hasattr(e1, 'salary')) # Returns true if 'salary' attribute exists
print (getattr(e1, 'name')) # Returns value of 'name' attribute
setattr(e1, 'salary', 7000) # Set attribute 'salary' at 8
delattr(e1, 'age') # Delete attribute 'age'
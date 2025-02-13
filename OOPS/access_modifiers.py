class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
# print (e1.__age)#error
print (e1._Employee__age)#accessing the private variable

print("Getter and Setter methods")
class Employee:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age
      return
   name = property(get_name, set_name, "name")
   age = property(get_age, set_age, "age")

e1=Employee("Bhavana", 24)
print ("Name:", e1.name, "age:", e1.age)

e1.name = "Archana"
e1.age = 23
print ("Name:", e1.name, "age:", e1.age)
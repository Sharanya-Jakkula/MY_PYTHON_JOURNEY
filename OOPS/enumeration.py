from enum import Enum,unique

class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   SCIENCE = 3
   SANSKRIT = 4
obj = subjects.MATHS
print (type(obj), obj.value)

print("String Based ENUM : ")
class subject(Enum):
   ENGLISH = "E"
   MATHS = "M"
   GEOGRAPHY = "G"
   SANSKRIT = "S"
   
obj = subject.SANSKRIT
print (type(obj), obj.name, obj.value)
print("\nIterating through the enum numbers : ")
for sub in subjects:
   print (sub.name, sub.value)
   
print("Using unique decorator : ")
@unique
class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   GEOGRAPHY = 3
   SANSKRIT = 4
#    raises error if there is a duplicate value

print("Using ENUM as callable class : ")
subjects = Enum("subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
for i in subjects:
    print(i)
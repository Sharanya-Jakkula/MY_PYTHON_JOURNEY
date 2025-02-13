# dynamic binding is the process of resolving a method or attribute at runtime, instead of at compile time.
class shape:
   def draw(self):
      print ("draw method")
      return

class circle(shape):
   def draw(self):
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()
   
print("duck-typing")
class circle:
   def draw(self):
      print ("Draw a circle")
      return

class rectangle:
   def draw(self):
      print ("Draw a rectangle")
      return

class area:
   def area(self):
      print ("calculate area")
      return

def duck_function(obj):
   obj.draw()

objects = [circle(), rectangle(), area()]
for obj in objects:
   duck_function(obj)
   
   #error

class Animal():
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def feed_on(self,food):
        self.food=food
    def property(self,prop):
        self.prop=prop
    def __str__(self):
        return 'The animal name is {}.\nIt feeds on {}.\nThe properties of the animal are {}'.format(self.name,self.food,self.prop)
if __name__=='__main__':
    name=input("Enter the name : ")
    food=input("What does it eat : ")
    color=input("What colour is it? ")
    prop=input("What can be the properties of the animal : ")
    animal=Animal(name,color)
    animal.property(prop)
    animal.feed_on(food)
    print("--------------------------------------")
    print(animal)
    print("--------------------------------------")

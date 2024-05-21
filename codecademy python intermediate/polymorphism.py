class Animal:
    def __init__(self,name):
        self.name=name


    def make_sound(self):
        print("{} says, Grrrr".format(self.name))



class Dog(Animal):
    def make_sound(self):
        print("{} says, ARGGHH".format(self.name))



class Cat(Animal):
    def make_sound(self):
        print("{} says, Meow".format(self.name))



list_of_animals=[Dog("Boxdel"),Cat("Bzik")]

for animal in list_of_animals:
    animal.make_sound()
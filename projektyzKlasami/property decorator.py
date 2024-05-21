class Box:
    def __init__(self,weight,height):
        self.__weight=weight



    def getWeight(self):
        return self.__weight


    def setWeight(self,weight):
        if weight >=0 :
            self.__weight=weight



    def delWeight(self):
        del self.__weight



    weight=property(getWeight,setWeight,delWeight,"Docstring for the 'weight' property")

box=Box(10,12)

print(box.weight)

box.weight=20

del box.weight

#z property decorator

class Pudlo:
    def __init__(self,waga):
        self.__waga=waga


    @property
    def weight(self):
        '''Docstring for the property'''
        return self.__waga


    @weight.setter
    def weight(self,nowa_waga):
        if nowa_waga>=0:
            self.__waga=nowa_waga

    @weight.deleter
    def weight(self):
        del self.__waga

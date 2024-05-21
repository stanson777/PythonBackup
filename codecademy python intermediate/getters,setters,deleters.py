class Employee:
    def __init__(self,name=None):
        self._name=name



    def get_name(self):
        return self._name


    def set_name(self,new_name):
        if isinstance(new_name,str):
            self._name=new_name
        else:
            raise TypeError

    def del_name(self):
        if self._name is not None:
            del self._name
        else:
            print("You dont have this name anymore since is None")


e1=Employee("Stanson")

print(e1.get_name())

e1.set_name("Marek")

print(e1.get_name())



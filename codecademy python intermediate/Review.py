from abc import ABC,abstractmethod

class AbstractEmployee:
    new_id=1
    def __init__(self):
        self.id=AbstractEmployee.new_id
        AbstractEmployee.new_id+=1


    @abstractmethod
    def say_id(self):
        pass



class User:
    def __init__(self):
        self._name=None


    @property
    def username(self):
        return self._name

    @username.setter
    def username(self,new_name):
        self._name=new_name

    @username.deleter
    def username(self):
        del self._name


class Meeting:
    def __init__(self):
        self.atendees=[]

    def __add__(self,employee):
        print(f"{employee.username} added to the meeting")
        self.atendees.append(employee.username)


    def __len__(self):
        return len(self.atendees)


class Employee(AbstractEmployee,User):
    def __init__(self,username):
        super().__init__()
        User.__init__(self)
        self.username=username

    def say_id(self):
        print(f"My id is {self.id}")

    def say_username(self):
        print(f"My username is {self.username}")
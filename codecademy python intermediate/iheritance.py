class Employee:
    new_id=1
    def __init__(self):
        self.id=Employee.new_id
        Employee.new_id+=1


    def say_id(self):
        print(f"My id is {self.id}")





class User:
    def __init__(self,username,role="Customer"):
        self.username=username

        self.role=role

    def say_user_id(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))
class Admin(Employee,User):
    def __init__(self):
        super().__init__()
        User.say_user_id(self,self.id,"Admin")
class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am a manager")

e1=Employee()
e2=Employee()
e3=Admin()

e1.say_id()

e2.say_id()
e3.say_id()

e4=Manager()
e4.say_id()
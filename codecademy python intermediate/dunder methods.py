class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)


    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)



v1=Vector(20,30)
v2=Vector(13,321)

v3=v1+v2

print(v3.x)
print(v3.y)
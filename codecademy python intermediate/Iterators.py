class MyNumbers:
    def __iter__(self):
        self.a=0
        return self


    def __next__(self):
        if self.a>=20:
            raise StopIteration
        x=self.a
        self.a+=1
        return x



myclass=MyNumbers()

myiter=iter(myclass)

while True:
    print(next(myiter))


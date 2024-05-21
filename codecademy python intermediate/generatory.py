def even_generator(x):
    i=0
    while i<=x:
        if i%2==0:
            yield i
        i+=1

def gen(n):
    for i in range(1,n+1):
        yield i**2

print(list(even_generator(69)))

g=gen(99999)

print(next(g))
print(next(g))
print(g.send(15))
print(next(g))
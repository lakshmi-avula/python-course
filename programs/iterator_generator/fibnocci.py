def fib(limit):
    a,b = 0,1
    while a<limit:      #using while
        yield a
        a,b = b,a+b


x = fib(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

#using for loop
print("Using for loop:")
for i in fib(5):
    print(i)



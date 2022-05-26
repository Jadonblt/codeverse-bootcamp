# def square(x):
#     return x*x


# def add(a,b):
#     c = a + b
#     print(c)

# def greater(a,b):
#     if(a>b):
#         return a
#     else:
#         return b

# def lesser(a,b):
#     if(a<b):
#         return a 
#     else:
#         return b

# def func(x,y,z):
#     if(z == 0):
#         print(greater(x,y))
#     elif(z == 1):
#         print(lesser(x,y))

# func(75,290,1)

x = 10
y = 20
def incrementBy(a, b, amount =10):
    a += amount
    b += amount
    return a, b

a ,b = incrementBy(x, y, 15)
print(a)
print(b)


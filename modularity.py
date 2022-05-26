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

# x = 10
# y = 20
# def incrementBy(a, b, amount =10):
#     a += amount
#     b += amount
#     return a, b

# a ,b = incrementBy(x, y, 15)
# print(a)
# print(b)

# def func(*args):
#     for x in args:
#         print(x)
#     print('Done')

# func(1,2,3,4)

# import math # this import

# a = math.sqrt(64)
# print(a)

# fibonacci series

def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        if(i == 0):
            print(a)
        elif(i == 1):
            print(b)
        else:
            c = a + b
            print(c)
            a = b
            b = c

fibo(7)
'''
Created on 2022. 4. 15.

@author: elink
'''
x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
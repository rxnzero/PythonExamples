'''
Created on 2022. 4. 15.

@author: elink
'''
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
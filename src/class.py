'''
Created on 2022. 4. 15.

@author: elink
'''
from pip._internal.cli.cmdoptions import pre
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def toString(self):
        print("name =", self.name, "age =", self.age, sep=" ", end="\n")

class Student(Person):
    pass        

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.toString()

p1 = Student("Jane", 18)
print(p1.name)
print(p1.age)
p1.toString()
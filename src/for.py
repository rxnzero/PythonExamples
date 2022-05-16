'''
Created on 2022. 4. 15.

@author: elink
'''
print(">> test case1")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print(x)

print("\n>> test case2")
for x in "banana":
    print(x)

print("\n>> test case3")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
            break

print("\n>> test case4")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
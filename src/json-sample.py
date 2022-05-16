'''
Created on 2022. 4. 15.

@author: elink
'''
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
"""
Python    JSON
dict    Object
list    Array
tuple    Array
str    String
int    Number
float    Number
True    true
False    false
None    null
"""
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print( "# default " )
print( json.dumps(x) )

print( "# indent " )
print( json.dumps(x, indent=4) )
print( "# indent, change sep " )
print( json.dumps(x, indent=4, separators=(". ", " = ")) ) # , -> . : => =
print( "# indent, order " )
print( json.dumps(x, indent=4, sort_keys=True) )
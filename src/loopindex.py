'''
Created on 2022. 4. 15.

@author: elink
'''
# list
colors = ["red", "green", "blue", "purple"]
# while
i = 0
while i < len(colors):
    print(colors[i])
    i += 1
    
#range of length    
for i in range(len(colors)):
    print(colors[i])
# for-in: the usual way
for color in colors:
    print(color)        

# What if we need indexes?
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# range of length
for i in range(len(presidents)):
    print("President {}: {}".format(i + 1, presidents[i]))

# enumerate
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))

# What if we need to loop over multiple things?
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
# enumerate
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))
#zip
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))
    
numbers = range(1,10)    
for n in numbers:
    print(n)

headers = ["header1","header2","header3"]
columns = ["row1", "row2", "row3"]
for header, rows in zip(headers, columns):
    print("{}: {}".format(header, ", ".join(rows)))

# ordering samples
lines = ["red", "green", "blue", "purple"]
for num, line in enumerate(lines):
    print("{0:03d}: {1:>10s}".format(num, line))
    print("{0:03d}: {1:^10s}".format(num, line))
    print("{0:03d}: {1:<10s}".format(num, line))
    
            
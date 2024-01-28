# A for loop is used for iterating over a sequence
# This is less like the for keyword in other programming languages, 
# and works more like an iterator method as found in other object-orientated programming languages.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

# BREAK :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
# CONTINUE :continue statement we can stop the current iteration of the loop, and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# RANGE : range()= a specified number of times
for x in range(6):
  print(x)
#HERE : i=(initialization,last-condtion,updation)
for x in range(2, 30, 3):
  print(x)

                                      # NESTED IN FOR-LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
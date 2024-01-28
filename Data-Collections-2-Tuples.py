#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
#Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#ACCESSING :
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry") #To check the presence of element
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#UPDATE : change values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Convert into a list:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# W.K.T tuples are unchangeable but after converting a tuple to a list, items can be changed &
#then convert back to tuple

# REMOVING
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# USING ASTERISK * 
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# MULTIPLY A TUPLE
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
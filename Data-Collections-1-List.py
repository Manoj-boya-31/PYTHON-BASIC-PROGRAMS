#Lists are used to store multiple items in a single variable.
#Lists are 1 of 4 built-in data types in Python to store data other 3 are Tuple, Set, and Dictionary
#Lists are created using square brackets
# LISTS ACT AS ARRAYS, STACKS, QUEUES in python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#ACESSING:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry"] #To check the presence of element
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#CHANGING:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

#ADDING : To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"] #The insert() method inserts an item at the specified index
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"] #To extend the list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#REMOVE: The pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"] #At specified index
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"] #del keyword also removes the specified index:
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"] #del entire list
del thislist
thislist = ["apple", "banana", "cherry"] #list still remains, but it has no content.
thislist.clear()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"] #Reverse thee list
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"] #Print all items by referring to their index number:
for i in range(len(thislist)):
  print(thislist[i])
thislist = ["apple", "banana", "cherry"] # using a while loop to go through all the index numbers
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#SORTING : sort() method that will sort the list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#You can also customize your own function by using the keyword argument key = function. The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#JOINING :
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]#using append
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
list1 = ["a", "b" , "c"]#extend method
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
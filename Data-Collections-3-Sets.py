#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# ACESSING : You cannot access items in a set by referring to an index or a key. 
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"} # add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# REMOVING : 
thisset = {"apple", "banana", "cherry"} # using remove
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"} #using discard
thisset.discard("banana")
print(thisset)

# JOINING SETS : union() method returns a new set with all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# Function: A block of code executed only when it is called
# In Python a function is defined using the DEF keyword
def greeting():
    print("hello")
    print("Have a nice wife")
greeting()

# Inside we can give information as arguments.
# arguments are also called as parameters
def greeting(name):
    print("hello "+name)
    print("Have a nice wife "+name)
greeting("Manoj")

# we can pass more than 1 parameters that to of different datatypes:
def greeting(name,age):
    print("hello "+name)
    print("Have a nice wife "+name+" and your age is "+str(age))
greeting("Manoj",21)

# Return values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
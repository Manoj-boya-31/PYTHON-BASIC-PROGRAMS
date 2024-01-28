                                    # ARGS : ARGUMENTS
# *ARGS = parameter that will pack all arguments into tuple useful so 
            # that function can accept varying amount of arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8,9,10))

def sub(*balayya):
    diff = 0
    for i in balayya:
        diff -= i
    return diff
print(sub(1,2,3,4,5,6,7,8,9,10))

# **KWARGS = parameter that will pack all arguments into dictionary useful so
            # that function can accept varying amount of keyword arguments

                                    # **KWARGS = Keyword Arguments
# This way the order of the arguments does not matter.
def my_function(first,middle,last):
  print("Hello "+first+" "+middle+" Do you have wife? "+last)
my_function(first="Manoj",middle="Boya",last="Yes")
my_function(last="Manoj",middle="Yes",first="Boya")

# You can also send arguments with the key = value syntax.
def my_function(**kwargs):
  print("Hello ")
  for key,value in kwargs.items():
    print(value)
my_function(last="Manoj",middle="KT",first="Boya")
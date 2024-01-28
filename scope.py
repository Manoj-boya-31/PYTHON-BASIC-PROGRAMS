# Scope : variable is only available from inside the region it is created
# local scope of that function, and can only be used inside that function.
# global scope, and can be used both inside and outside of the function of the program.
# SAME LIKE GLOBAL VARIABLE & LOCAL VARIABLE IN C LANGUAGE
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

print(x) # x is global here.represented by global keyword
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
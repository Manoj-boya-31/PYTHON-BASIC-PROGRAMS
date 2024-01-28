# The elif keyword is way of saying "if the previous conditions were not true, then try this condition".
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b: # here meaning of elif means = or may be
  print("a and b are equal")
else:
  print("a is greater than b")

# AND : and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# OR : or keyword is a logical operator, and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# NOT : not keyword is a logical operator, and is used to reverse the result of the condition
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

                            # NESTED IF : if statements in if condition
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

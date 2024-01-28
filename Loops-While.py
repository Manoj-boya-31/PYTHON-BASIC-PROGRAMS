# WHILE : while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1

# BREAK
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# CONTINUE
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# ELSE in while loop
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
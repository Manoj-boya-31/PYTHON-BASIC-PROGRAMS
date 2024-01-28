#Variable is container for a value. Behaves as the value which contains: STRING, INTEGER, FLOAT, BOOLEAN

first_name ='manoj'
last_name ='boya'
print(first_name+" "+last_name)
print(type(first_name))#prints what type of datatype

age=20
age+=1
#print("age : "+age) --- here you will get error because age should be typecasted to str(age)
#before printing anything in print line, it should be converted to str(), So
print("age : "+str(age))
print(type(age))

height=5.1
print("height : "+str(height))
print(type(height))

Brave=True
print("is he very brave :"+str(Brave))
print(type(Brave))

#MULTIPLE ASSIGNMENT allows us to assign multiple variables at same line of code
Name,NoOfWives,attractive="Manoj.T",2,True
print("Name is "+str(Name)+" Who has "+str(NoOfWives)+" Wives who are very attractive? "+str(attractive))

# Now without multiple assignment for same value, :
Cars=Bikes=Homes=3
print("No of cars :"+str(Cars))
print("No of bikes :"+str(Bikes))
print("No of homes :"+str(Homes))

print(len(Name))
print(Name.find('T'))
print(Name.capitalize())
print(Name.upper())
print(Name.lower())
print(Name.isdigit())
print(Name.isalpha())
print(Name.count('o'))
print(Name.replace('.','-'))
print(Name*3)

#typecasting: converting 1 datatype to another datatype

x=1 #int
y=2.0 #float
z='3' #string

print(x)
print(y)
print(z*3)

x=float(x)
y=int(y)
z=int(z)

print(x)
print(y)
print(z*3)
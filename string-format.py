#The format() method allows you to format selected values of a string.
# add placeholders (curly brackets {}) in the text, and run the values through the format() method:

fnmae='Vijay'
lname="Thalapathy"
age=45
print("My hero is {} {} and my age is {}".format(fnmae,lname,age))

# You can add parameters inside the curly brackets to specify how to convert the value:
print("My hero is {0} {1} and my age is {2}".format(fnmae,lname,age))

                                        #STRING REVERSE METHOD:
#BUT, IN PYTHON TO REVERSE ANY STRING THE ABOVE STEP-INDEXING-METHOD HELPS:
#very simple trick = :
name='manoj boya'
Reverse=name[::-1]
print(Reverse)

                                        #STRING CONCATENATION:
# Very simple trivk is use + operator:
first_name ='manoj'
last_name ='boya'
print(first_name+" "+last_name)
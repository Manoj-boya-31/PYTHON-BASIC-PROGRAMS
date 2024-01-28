#slicing : create a substring by extracting elements from another string
# either by INDEXING[] (or) by SLICE()
#[START_INDEX : STOP_INDEX : STEP_INDEX]
name='manoj boya'
#REMEMBER, starting index is inclusive and stopping index is exclusive,so put stopping index ahead 1 more

first_name=name[0:5]   #Here if we dont provide starting index, Python by default assumes it as 0th index
last_name=name[6:10]

print(first_name)
print(last_name)

nickname=name[0:10:2]
                #In Step index, here above it prints every 2nd character, 1 after 1 count 
print(nickname)

nickname=name[0:10:3] #here it prints every 3rd character, 1 after 1 count
print(nickname)

                #BUT, IN PYTHON TO CONCATENATE ANY STRING THE ABOVE STEP-METHOD HELPS:

Reverse=name[::-1]
print(Reverse)

                                    #SLICING SYNTAX:
#SLICING SYNTAX: Same as indexing, but here flower brackets() and commas, will be used = slice(,)
#here negative indexing can also be used.
website ="htpp://google.com"
slice=slice(7,-4)
print(website[slice])
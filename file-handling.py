# FIRST CREATE A FILE IN ANY FOLDER AND GIVE THE PATH OF THAT FILE IN THE BELOW CODE:

# TO CHECK THE FILE EXISTING OR NOT
import os
path = "C:\\Visual Studio\\VS code\\balayya.txt"

if os.path.exists(path):
    print("Given path exists")
else:
    print("Given path does not exists")

# TO READ THE FILES
with open('balayya.txt') as file:
    print(file.read())

# TO UPDATE THE DATA IN A FILE
with open('balayya.txt', 'a') as file:
    file.write("\nI am a fan of Balayya")

# TO DELETE THE FILE
#import os
#os.remove("balayya.txt")
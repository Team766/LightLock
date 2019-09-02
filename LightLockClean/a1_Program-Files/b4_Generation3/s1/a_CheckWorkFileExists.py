#Checks that the static working file exists

#Required Testing Imports
import sys

#Function
def checkFileExists(path):
    
    a = 0
    
    try:
        with open(path, 'r'):
            a = 1
    except:
        a = -1
    
    if a == -1:
        sys.exit("File Does Not Exist, please check name and filestrucuture")
    
    return 0
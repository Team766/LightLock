#Test Notes: File Interperts Successfully
#Test Notes: Does not output error if file is not of correct type or nonexistant. Format works, though.



def testFileExist(testFile):
    try:
        with open(testFile, 'r'):
            return 1
    except:
        return -1


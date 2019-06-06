#Removable Testing Imports
import cv2

#Test Notes: File Interperts Successfully
#Test Notes: Does not output error if file is not of correct type or nonexistant. Format works, though.



def loadFile(testFile):
    try:
        with open(testFile, 'r'):
            workImg = cv2.imread(testFile,cv2.IMREAD_GRAYSCALE)
            return workImg
    except:
        print("File Does Not Exist. Check Path")
        
        return "File Not Found"
    return 0

loadFile("C:\\Users\team766\Python Projects\LightLock\0_\0_2_\1024px-3-2-circular.png")
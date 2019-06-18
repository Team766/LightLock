#All Required Imports of external libraries
import numpy as np
import cv2
import math
import sys


#Import Data Classes Preselection
import c1_Preselection.d2_RobotPosition as c1d2
#import c1_Preselection.d3_FieldInformation as c1d3
#import c1_Preselection.d4_Light as c1d4
#Import Homebrew Classes AQUIRE_DATA




#Import Seperate Functions
import c1_Preselection.d6_robotStartingPoint as c1d6
import c2_AquireData.d1 as c2d1
import c2_AquireData.d3_spaceSelection as c2d3

#Create Robot and Field Implementations
robot = c1d2.RobotPosition(10,5,-90)
#fieldteststupid = c1d3.FieldInformation()


#Designate Starting Parameters
work_file = "C:/Users/team766/Documents/Blender Stuff/test6.png" #Add file to test path in here
start_pos = "rl" #Chose Starting Position (rr,rc,rl,br,bc,bl)
height_of_ceiling = 70

#Tunable Parameters
color_low_bound = 205 #Anything above this will still remove the rotation gray


#Architecture Step 1:Gather Data
#c1d6.RobotStartingPoint(start_pos,robot)

if c2d1.testFileExist(work_file) == -1:
    sys.exit("File Does Not Exist, please check name and filestrucuture")
elif c2d1.testFileExist(work_file) != 1:
    sys.exit("c2d1 filechecker has failed in a completely unexpected way. Redo your code, numbskull")
else:
    working_img = cv2.imread(work_file,0) #This implies I should check for a propper image file.
    print("Image Exists")

#I think that this works properly, but I really don't know. I need generated test data to determine, and I dont have that.

#cpix = c2d3.convertCornerAngles(1920,180,*c2d3.pixelRange(height_of_ceiling,robot.x_pos,robot.y_pos))
#working_img = c2d3.trimInput(working_img,robot.heading,int(cpix[0]),int(cpix[1]),int(cpix[2]),int(cpix[3]))

#Architecture Step 2: Preprocess Data
#working_img = cv2.inRange(working_img,color_low_bound,255) #Strips all non-white parts of the image out. Must be tuned


cv2.imshow("3",working_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Architecture Step 3: Extract Information from Data


#Architecture Step 4: Determine Location from Information


#Architecture Step 5: Send Information to Robot


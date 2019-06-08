#All Required Imports of external libraries
import numpy as np
import cv2
import math
import sys


#Import Data Classes Preselection
import c1_Preselection.d2_RobotPosition as c1d2
#import c1_Preselection.d3_FieldInformation as c1d3
import c1_Preselection.d4_Light as c1d4
#Import Homebrew Classes AQUIRE_DATA




#Import Seperate Functions
import c1_Preselection.d6_robotStartingPoint as c1d6
import c2_AquireData.d1 as c2d1

#Create Robot and Field Implementations
robot = c1d2.RobotPosition(0,0,0)
#fieldteststupid = c1d3.FieldInformation()


#Designate Starting Parameters
work_file = "C:/Users/team766/Python Projects/LightLock/0_/0_2_/1024px-3-2-circular.png" #Add file to test path in here
start_pos = "rl" #Chose Starting Position (rr,rc,rl,br,bc,bl)

#Architecture Step 1:Gather Data
c1d6.RobotStartingPoint(start_pos,robot)

if c2d1.testFileExist(work_file) == -1:
    sys.exit("File Does Not Exist, please check name and filestrucuture")
elif c2d1.testFileExist(work_file) != 1:
    sys.exit("c2d1 filechecker has failed in a completely unexpected way. Redo your code, numbskull")
else:
    working_img = cv2.imread(work_file,0) #This implies I should check for a propper image file.





#Architecture Step 2: Preprocess Data


#Architecture Step 3: Extract Information from Data


#Architecture Step 4: Determine Location from Information


#Architecture Step 5: Send Information to Robot


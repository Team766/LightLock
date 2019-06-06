#All Required Imports of external libraries
import numpy as np
import cv2
import math


#Import Data Classes
from c1_Preselection.d2 import robotPosition
from c1_Preselection.d3 import fieldInformation
#import c1_Preselection.d5

#Create Robot and Field Implementations
robot = robotPosition(0,0,0)
field = fieldInformation(50)

#Chose File to Test
workFile = "" #Add file to test path in here

def RobotStartingPoint(TWO_CHAR_ID,Class_Name):
    if TWO_CHAR_ID == "br":
        robot.updatePosition(1,1,1)
    elif TWO_CHAR_ID == "bc":
        robot.updatePosition(2,2,2)
    elif TWO_CHAR_ID == "bl":
        robot.updatePosition(3,3,3)
    elif TWO_CHAR_ID == "rr":
        robot.updatePosition(-1,-1,-1)
    elif TWO_CHAR_ID == "rc":
        robot.updatePosition(-2,-2,-2)
    elif TWO_CHAR_ID == "rl":
        robot.updatePosition(-3,-3,-3)
    else:
        return -1 #For Error Detection
    
    Class_Name.updatePosition(0,0,0)
    print(Class_Name.returnPosition())
    return 0 

RobotStartingPoint("rl",robot)
#All Required Imports of external libraries
import numpy as np
import cv2
import math


#Import Data Classes
import c1_Preselection.d2_RobotPosition as c1d2
import c1_Preselection.d3_FieldInformation as c1d3
import c1_Preselection.d6_robotStartingPoint as c1d6
import c1_Preselection.d4_Light as c1d4

#Create Robot and Field Implementations
robot = robotPosition(0,0,0)
field = fieldInformation(50)

#Chose File to Test
work_file = "" #Add file to test path in here 

#Chose Starting Position (rr,rc,rl,br,bc,bl)
start_pos = "rl"


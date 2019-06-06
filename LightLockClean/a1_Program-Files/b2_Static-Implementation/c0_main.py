#All Required Imports of external libraries
import numpy as np
import cv2
import math


#Import Data Classes Preselection
import c1_Preselection.d2_RobotPosition as c1d2
import c1_Preselection.d3_FieldInformation as c1d3
import c1_Preselection.d4_Light as c1d4
#Import Homebrew Classes AQUIRE_DATA




#Import Seperate Functions
import c1_Preselection.d6_robotStartingPoint as c1d6

#Create Robot and Field Implementations
robot = robotPosition(0,0,0)
field = fieldInformation(50)


#Designate Starting Parameters
work_file = "" #Add file to test path in here
start_pos = "rl" #Chose Starting Position (rr,rc,rl,br,bc,bl)

#Architecture Step 1:Gather Data


#Architecture Step 2: Preprocess Data


#Architecture Step 3: Extract Information from Data


#Architecture Step 4: Determine Location from Information


#Architecture Step 5: Send Information to Robot


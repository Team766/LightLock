#Will Analyse Static Image and output position given recent previous info




#Necessary library imports
import numpy as np
import math
import cv2

#Necessary File/Function Imports

#Image
    #Checks Existance of File - b4c1d1
from c1_Image.d1_checkFileExistance import checkFileExists
    #Imports Image as Grayscale
#None
    #Determines size of Image
#None

#Process
    #Cuts image to field only
    #Outlines Lights
    #Identify Each Light
    #Find Center of Light
    #Output Heading and ID of each light to /Extract




#Extract

#Output

#Constant Starting Parameters
height_of_ceiling = 70
work_file = "C:/Users/team766/Documents/Blender Stuff/test5.png" #Image to analyse
height_of_camera = 2

#Changable Parameters
robot_heading = 0
last_known_position = (0,0) #Previous Position Output
estimated_position = (0,0) #Changes using other information and Kalman Filter (Inertial Info)

#Image
    #Checks Existance of File
checkFileExists(work_file)
    #Imports image as grayscale
working_image = cv2.imread(work_file,0)
    #Determines Size of Image
length_of_working_image,width_of_working_image = working_image.shape

#Process


















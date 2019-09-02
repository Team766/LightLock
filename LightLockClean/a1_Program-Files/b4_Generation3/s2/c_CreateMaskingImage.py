#Takes in a set of points, and creates the masking image for those points

#Standard imports
import numpy as np
import cv2

#Inputs:
    #Upper Image Size, target array
def createMask(image_width,image_height,target_np_array): #Input is base #image width, image height, points array
    
    width = image_width
    height = image_height
    
    mask = np.zeros((height,width),dtype = np.uint8)
    
    pts = target_np_array
    #pts = pts.reshape((-1,1,2))
    #cv2.polylines(mask,[pts],True,(255,255,255))
    cv2.fillPoly(mask,[pts],255, lineType = 8, shift=0)
    return mask
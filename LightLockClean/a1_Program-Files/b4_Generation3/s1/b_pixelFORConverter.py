#Converts pixels from 0,0 at top left to center of image, and then back in a different function

#Standard Imports
import numpy as np


def baseToRevised(pixel,image_width,image_height):
    x = pixel[0]
    y = pixel[1]
    
    half_w = int(image_width/2)
    half_h = int(image_height/2)
    
    x = x - half_w
    y = y - half_h
    
    return np.array([x,y])

def revisedToBase(pixel,im_w,im_h):
    x = pixel[0]
    y = pixel[1]
    
    half_w = int(im_w/2)
    half_h = int(im_h/2)
    
    x = x + half_w
    y = y + half_h
    
    return np.array([x,y])
    
    
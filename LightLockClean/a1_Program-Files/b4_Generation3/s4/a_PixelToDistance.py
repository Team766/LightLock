#Takes a pixel value and returns a distance. Just a distance!

#Standard Imports
import math


def pixelToDistance(height,focal_length,pixel): #Height in "distance units", pixel is numpy array #NEEDS REVISED PIXEL INPUTS
    r = math.sqrt(pixel[0]**2 + pixel[1]**2)
    
    f = focal_length 
    theta = 2*(math.asin(r/(2*f))) #This should not be greater than 1, so if r > f something is very wrong
    zulu = height * math.tan(theta)
    
    return zulu
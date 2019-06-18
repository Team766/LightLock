import math
import cv2

#Determines angle from robot to each corner of ceiling, with no padding
def pixelRange(height, x_now, y_now): #This is outputting an angular measurement
    #Angle to +x direction
    xPlusAngle = math.degrees(math.atan2(27-x_now, height))
        
    #Angle to -x direction
    xMinusAngle = math.degrees(math.atan2(-27-x_now, height))
        
    #Angle to +y direction
    yPlusAngle = math.degrees(math.atan2(13.5-y_now, height))
        
    #Angle to -y direction
    yMinusAngle = math.degrees(math.atan2(-13.5-y_now, height))
        
    return (xPlusAngle, xMinusAngle, yPlusAngle, yMinusAngle)

def convertCornerAngles(pixels,degrees,xp,xm,yp,ym): #In degrees,from Field class
    conversionFactor = pixels/degrees #pixels/degrees
    xpOut = xp * conversionFactor
    xmOut = xm * conversionFactor
    ypOut = yp * conversionFactor
    ymOut = ym * conversionFactor
    
    return (xpOut/2,xmOut/2,ypOut/2,ymOut/2)

def trimInput(work_img,hdg,xpos,xmin,ypos,ymin):
    #work_img is the input image, hdg is the current heading of the robot, xp is max necesary x range, and etc.
    rows,cols = work_img.shape
    #M = cv2.getRotationMatrix2D((cols/2,rows/2),-hdg,1)
    #work_img = cv2.warpAffine(work_img,M,(cols,rows))
    #Take Region of interest of that image corrisponding to determined points
    xsize = 960/2
    ysize = 540/2
    
    ypos = int(ysize - ypos)
    ymin = int(ysize - ymin)
    xpos = int(xsize - xpos)
    xmin = int(xsize - xmin)
    work_img = work_img[ypos:ymin,xpos:xmin]
    #Rotate Img back by hdg
#    rows,cols = work_img.shape
#    M2 = cv2.getRotationMatrix2D((cols/2,rows/2),hdg,1)
#    work_img = cv2.warpAffine(work_img,M2,(cols,rows))
    #work_img = work_img[ypos:ymin,xpos:xmin]
    #send Image on in return
    return work_img #This should be image, no other output data, bitches I'm damn good



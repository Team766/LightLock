import math
import cv2

#Determines angle from robot to each corner of ceiling, with no padding
def pixelRange(height, x_now, y_now):
    #Angle to +x direction
    xPlusAngle = math.degrees(math.atan2 (27-x_now, height))
        
    #Angle to -x direction
    xMinusAngle = math.degrees(math.atan2(-27-x_now, height))
        
    #Angle to +y direction
    yPlusAngle = math.degrees(math.atan2(13.5-y_now, height))
        
    #Angle to -y direction
    yMinusAngle = math.degrees(math.atan2(-13.5-y_now, height))
        
    return (xPlusAngle, xMinusAngle, yPlusAngle, yMinusAngle)

def convertCornerAngles(xp,xm,yp,ym): #In degrees,from Field class
    conversionFactor = 1920/180 #pixels/degrees
    xpOut = xp * conversionFactor
    xmOut = xm * conversionFactor
    ypOut = yp * conversionFactor
    ymOut = ym * conversionFactor
    
    return (xpOut,xmOut,ypOut,ymOut)

def trimInput(work_img,hdg,xpos,xmin,ypos,ymin):
    #work_img is the input image, hdg is the current heading of the robot, xp is max necesary x range, and etc.
    rows,cols = work_img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),-hdg,1)
    work_img = cv2.warpAffine(work_img,M,(cols,rows))
    #Take Region of interest of that image corrisponding to determined points
    work_img = work_img[xpos:xmin,ypos:ymin]
    #Rotate Img back by hdg
    rows,cols = work_img.shape
    M2 = cv2.getRotationMatrix2D((cols/2,rows/2),hdg,1)
    work_img = cv2.warpAffine(work_img,M2,(cols,rows))
    #send Image on in return
    return work_img #This should be image, no other output data, bitches I'm damn good



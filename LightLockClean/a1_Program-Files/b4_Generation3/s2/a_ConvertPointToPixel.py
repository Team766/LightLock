#Takes a field-centric x-y position at height, and converts that into a pixel
#Allows a small outline of the AOE to be created
#Only correct for equiangular fisheye of 180 degree coverage!
#Change if camera changes


#Standard Imports
import math
import numpy as np


def pointPixelEA(tgt,tgt_h,robot,robot_h,robot_heading): #m,m,m,m,m,m,radians; target position, target height, robot position, robot height, robot heading
    focal_length = 214.1528 #pixels #Change this if camera profile changes, will fuck things if not done, keep hardcoded
    
    #Gives height for later math, eliminate for performace, keep for elevated accuracy
    delta_height = tgt_h - robot_h
    
    POI_loc = (tgt[0],-1*tgt[1])
    robot_loc = robot
    
    heading = robot_heading
    
   #Define Local Functions
    def getPictureRadius(focal_length_z,robot_heading_z,robot_loc_z,POI_loc_z,delta_height_z): #Gives radius in pixels of desired point
        radius = math.sqrt((POI_loc_z[0] - robot_loc_z[0])**2 + (POI_loc_z[1] - robot_loc_z[1])**2 )
        
        #Find Zenith Angle
        zenith_angle = math.pi/2 - math.atan2(delta_height_z,radius)
        
        #Corner overlap testing
            #Defines radius on sensor based on focal length and zenith angle, equisolid testing, 180 FOV
        r = 2 * focal_length_z * math.sin(zenith_angle * 0.5)
    
        return r
    
    #Finds angle between tgt vector and optical axis
    def findTheta(POI_loc_z,robot_loc_z,robot_heading_z):
        theta = (math.atan2(POI_loc_z[1] - robot_loc_z[1],POI_loc_z[0] - robot_loc_z[0]) + robot_heading_z)%(2*math.pi)
        return theta
    
    #Converts from polar to cartesian coordinates, outputs x-coordinate
    def polarCartesianX(theta_z,point_radius_z):
        x = point_radius_z * math.cos(theta_z)
        return x
    
    #Converts from polar to cartesian coordinates, outputs y-coordinate
    def polarCartesianY(theta_z,point_radius_z):
        y = point_radius_z * math.sin(theta_z)
        return y 
    
    #Determines how far out the target pixel is, in pixels. 
    point_radius = getPictureRadius(focal_length,heading,robot_loc,POI_loc,delta_height)
    #Outputs theta
    zulu = findTheta(POI_loc,robot_loc,heading)
    
    #Final Calculation
    pixel_x = polarCartesianX(zulu,point_radius)
    pixel_y = polarCartesianY(zulu,point_radius)
            
    return np.array([pixel_x,pixel_y]) #Returns revised pixel position

#NOTES:
    '''
    Field is measured with y axis in starting direction of robot from red, with x 90 degrees clockwise
    from that. Robot Angle is measured with y towards front of robot, x 90 degrees clockwise.
    Heading is the differental between each y axis
    '''
'''Given a point, adds a constant to create a np array of points surrounding the
   relevant center point'''
   
#Standard Imports
import numpy as np

#Start Function Definition
def quadPointCreator(centerpoint,im_w,im_h): #Centerpoint in revised,image width,image height
    cp_x = centerpoint[0] + im_w/2
    cp_y = centerpoint[1] + im_h/2
    
    constant = 40 #pixels, tune this
    
    #TODO: Make constant depend on the distance away from the robot of the target point
        #Note: Kind of boring, do some other time.

    cpxp = cp_x + constant 
    cpxm = cp_x - constant
    
    cpyp = cp_y + constant
    cpym = cp_y - constant
    
    return np.array([[cpxp,cpyp],
                    [cpxp,cpym],
                    [cpxm,cpym],
                    [cpxm,cpyp]],dtype = np.int32) #Outputs in base
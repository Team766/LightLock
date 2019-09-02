#Function to apply circle intersection
    #Inputs:
        #point 1, distance 1, point 2, distance 2
        #np.a, float, np.a, float

#Standard imports
import math
import numpy as np
        
def circleIntersection(point_1,dist_1,point_2,dist_2): #*1

    x_0 = point_1[0]
    y_0 = point_1[1]
    r_0 = dist_1
    
    x_1 = point_2[0]
    y_1 = point_2[1]
    r_1 = dist_2
    
    d = math.sqrt((x_1-x_0)**2 +(y_1-y_0)**2)
    a = (r_0**2 - r_1**2 + d**2)/(2*d)
    h = np.sqrt(r_0**2 - a**2)
    
    x_2 = x_0+a*(x_1-x_0)/d   
    y_2 = y_0+a*(y_1-y_0)/d
    
    x_31=x_2 + h*(y_1-y_0)/d
    y_31=y_2 - h*(x_1-x_0)/d
    
    x_32=x_2 - h*(y_1-y_0)/d
    y_32=y_2 + h*(x_1-x_0)/d
    
    
    return (x_31,y_31),(x_32,y_32)

#NOTES: Does not test for irregular conditions, which really shouldn't happen.
    #It should be mathmatically impossible
    #But they keep hapending, so it is critical to do so

#SOURCES: https://stackoverflow.com/questions/3349125/circle-circle-intersection-points *1

    
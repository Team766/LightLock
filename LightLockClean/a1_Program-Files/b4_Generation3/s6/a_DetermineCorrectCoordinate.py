#Determines which solution is correct from the previous stage
        
#Standard imports
import numpy as np
#import math #Unused

#Inputs: estimated position of robot, first solution from previous, second solution
    #np.a, tuple, np.a
def checkSolutions(estimated_position,solve_1,solve_2):
    a = estimated_position[0]
    b = estimated_position[1]
    
    a_alfa = a - solve_1[0]
    a_bravo = a - solve_2[0]
    
    b_alfa = b - solve_1[1]
    b_bravo = b - solve_2[1]
    
    if (a_alfa**2 + b_alfa**2) <= (a_bravo**2 + b_bravo**2):
        return (solve_1[0],solve_1[1])
    else:
        return (solve_2[0],solve_2[1])
    
#NOTES: If solve 1 is closer to the inertial estimate, output it. Otherwise, output the other one
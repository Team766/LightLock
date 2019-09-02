#The main file for the entire Generation 3 Lightlock. Run this to do shit.
#Collin Brahana

'''
Plan
1.Take Image
    1.Check for image existance
    2.Import as grayscale
2.Isolate each light
    1.Draw Mask around each light approximately
    2.Convert image to binary with threshhold
    3.Create Contour
3.Determine center point of each isolated light
    1.Draw circle around largest contour of each suspected light
        1.Check that it is the light, and not something else
    2.Use center point of circle as output
4.Find distance to each center point
    1. Use angle and fisheye properties to calculate distance accurately
5.Apply circle intersection to each distance and point coordinates
    1.Really simple, just 1 module
    2.Maybe 2, for error checking
6.Determine Current Coordinate
    1.Really simple, which point is closest to estimated inertial position?
7.Output Information
    1.Print statement
'''

#Basic Imports
import math
import numpy as np
import cv2

#Step Imports

    #Step 1 Imports
        #Checks work file for existance
import s1.a_CheckWorkFileExists as s1a #Checks work file for existance
import s1.b_pixelFORConverter as s1b
        #Loads image as variable
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
    
    #Step 2 Imports
        #Allows point to be matched to pixel
        #DONE: Heading Testing, in F-FOR:::Functional, in all desired senses
import s2.a_ConvertPointToPixel as s2a #Can take arbitrary desired point and isolate pixel closest to it
        #Creates points surrounding light in math for easy POI selection
            #TODO: Create function to determine constant size for cheap point selection
                #Note: Boring
            #TODO: TEST IN SITU
import s2.b_RectangularBorderPoints as s2b
        #Creates masking image
            #Given image width, image height, and list of points to form quad mask
import s2.c_CreateMaskingImage as s2c
         #Applies mask to image
#https://stackoverflow.com/questions/25074488/how-to-mask-an-image-using-numpy-opencv
        #Thresholds image after mask
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
        #Creates Contour of light in threshholded masked image
#https://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html
    
    #Step 3 Imports
        #Function takes contour and returns the point that the light ocpuies
import s3.a_FindContourCenter as s3a
    #Step 4 Imports
        #Converts Pixel to distance given ceiling height
import s4.a_PixelToDistance as s4a
    #Step 5 Imports
        #Triangulates
import s5.a_ApplyCircleIntersection as s5a
    #Step 6 Imports
import s6.a_DetermineCorrectCoordinate as s6a
    #Step 7 Imports

#Hardware Dependent Variables
focal_length = 214.1528 #HINT: Change this to correct value, then delete todo #Focal length of camera, fixed, in pixels

#Settable Variables
    #Robot Position, best guess
est_pos = (-10,0) #Change this to test different positions, KEEP AS TUPLE
robot_heading = 0 #Sets heading of the robot, for rotation testing

    #Heights
height_light = 10
height_camera = 0

#FAST find this easily to reset
working_image = "C:/Users/team766/Documents/Blender Stuff/test14.png" #String of working image, \ signs reversed because fuck DOS
light_one = (7,7)
light_two = (-7,7)

###############################################START OF "DOING THINGS" CODE

#Checks that image exists
s1a.checkFileExists(working_image) 

#Imports image as grayscale
working_var = cv2.imread(working_image,0)

#Finds shape of working variable
working_var_shape = working_var.shape
working_var_height = working_var_shape[0]
working_var_width = working_var_shape[1]

#Determines where the relevant light pixels are based on inertial data
light_one_pixel_inertial = s2a.pointPixelEA(light_one,height_light,est_pos,height_camera,robot_heading) #TIP: This is good
light_two_pixel_inertial = s2a.pointPixelEA(light_two,height_light,est_pos,height_camera,robot_heading) 

#Computes border region knowing the thought center point
light_one_border_region = s2b.quadPointCreator(light_one_pixel_inertial,working_var_width,working_var_height) 
light_two_border_region = s2b.quadPointCreator(light_two_pixel_inertial,working_var_width,working_var_height)

#TEST:
print("border 1:\n" ,light_one_border_region)
print("border 2:\n" ,light_two_border_region)
#ENDTEST:

#Removes everything outside those border regions
light_one_mask = s2c.createMask(working_var_width,working_var_height,light_one_border_region)
light_two_mask = s2c.createMask(working_var_width,working_var_height,light_two_border_region)

working_var_masked_one = cv2.bitwise_and(working_var,light_one_mask)
working_var_masked_two = cv2.bitwise_and(working_var,light_two_mask)

cv2.imshow("a", working_var_masked_one)
cv2.imshow("b", working_var_masked_two)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Threshholds image
_,working_var_threshed_one = cv2.threshold(working_var_masked_one,200,255,cv2.THRESH_BINARY)
_,working_var_threshed_two = cv2.threshold(working_var_masked_two,200,255,cv2.THRESH_BINARY)


#Finds contours from thresholded images
_, working_contours_one,_ = cv2.findContours(working_var_threshed_one,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
_, working_contours_two,_ = cv2.findContours(working_var_threshed_two,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#Takes contour and finds center
light_one_pixel_center = s3a.contourVector(working_contours_one[0])
light_two_pixel_center = s3a.contourVector(working_contours_two[0])

light_one_pixel_center = s1b.baseToRevised(light_one_pixel_center,working_var_width,working_var_height)
light_two_pixel_center = s1b.baseToRevised(light_two_pixel_center,working_var_width,working_var_height)

#Takes center of contour and finds distance to robot
light_one_distance = s4a.pixelToDistance(height_light-height_camera,focal_length,light_one_pixel_center) #XXX: Garbage In
light_two_distance = s4a.pixelToDistance(height_light-height_camera,focal_length,light_two_pixel_center)

print("light one distance:" ,light_one_distance,)
print("light two distance:" ,light_two_distance,)

possible_locations = s5a.circleIntersection(light_one,light_one_distance,light_two,light_two_distance) #TIP: This works


print("Possible Locations:" ,possible_locations,)
probable_location = s6a.checkSolutions(est_pos,*possible_locations)

print("Probable Location:" ,probable_location,)




#Things I need to do!!!
#TODO: Fix s5 error handling and irregular circles
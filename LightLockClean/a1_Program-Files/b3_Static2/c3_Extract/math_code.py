import math

PI = 3.141592653

def generatePointTwo(t1,tangent): #Creates a second point based off of heading
    #Takes in first point as (x,y) tuple, and heading in radians
    t1_1 = t1[0]
    t1_2 = t1[1]
    
    t1out = t1_1 +1
    t2out = t1_2 - tangent
    
    return (t1out,t2out)

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    #Finds intersection of two lines defined by two points each
    #1 is light_one, 2 is addition to light_one
    #3 is light_two, 4 is addition to light_two
    a,b,c,d = x1,y1,x2,y2
    e,f,g,h = x3,y3,x4,y4
    
    P_x = ((a*d-b*c)*(e-g)-(a-c)*(e*h-f*g))/((a-c)*(f-h)-(b-d)*(e-g))
    P_y = ((a*d-b*c)*(f-h)-(b-d)*(e*h-f*g))/((a-c)*(f-h)-(b-d)*(e-g))
    return (P_x,P_y)

def lightRelativeHeading(vision_heading,robot_heading_f):
    return (vision_heading + robot_heading_f + 180)%360

def degreesToRadians(degrees):
    return degrees * (PI/180)

light_one = (-4,4)
light_two = (-4,-4)

#Accurate Gyro Heading of Robot
robot_heading = 0


#Headings in degrees relative to camera, taken from camera data
vision_heading_one = 180+63.475
vision_heading_two = 180-63.475

#give headings relative to lights in degrees
light_heading_one = lightRelativeHeading(vision_heading_one,robot_heading)
light_heading_two = lightRelativeHeading(vision_heading_two,robot_heading)

#Convert degrees to radians
light_heading_one = degreesToRadians(light_heading_one)
light_heading_two = degreesToRadians(light_heading_two)


#Find slope ratio
h_1 = math.tan(light_heading_one)
h_2 = math.tan(light_heading_two)

P1_2 = generatePointTwo(light_one,h_1)
P2_2 = generatePointTwo(light_two,h_2)

print(findIntersection(*light_one,*P1_2,*light_two,*P2_2))
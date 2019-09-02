#Takes in contour, outputs a center for heading-analysis
import cv2

def contourVector(contour):
    (x,y),_ = cv2.minEnclosingCircle(contour)
    return (x,y) #OUTPUT IS BASE

'''
#NOTES: 
This works because in an equidistant fisheye, the heading of a point will
stay unchanged, while the distance will decreace the further from center that
point is. This means that as long as no lights overlap the optical axis, the 
points along the axis through the center will be compressed from a normal circle,
while the points along the perpendicular radial axis will not. I have a pseudoproof
for this, but what it means is that if you draw a line from image center through
the center of the contour as axis h, and a circle perpendicuar to axis a and through
the points of the contour furthest from a as axis b, then a circle that touches the 
points contacted by axis b will always have it's center in the center of the lights,
both optically and physically. It is an extremely cheap method to find the center
of this sort of pseudoelipse created by the lens.

IT WILL NOT WORK FOR NON-CIRCULAR LIGHTS OR OTHER LENS TYPES!
'''
class FieldInformation:
    
    def __init__(self, lightHeight):
        self.blueRefCorner = (27.0,-13.5)
        self.blueStandCorner = (27.0,13.5)
        self.redRefCorner = (-27.0,-13.5)
        self.redStandCorner = (-27.0,13.5)
        self.height = lightHeight
        
        return None
    
    #Determines angle from robot to each corner of ceiling, with no padding
    def pixelRange(self, x_now, y_now):
        #Angle to +x direction
        xPlusAngle = math.degrees(math.atan2 (27-x_now,self.height))
        
        #Angle to -x direction
        xMinusAngle = math.degrees(math.atan2(-27-x_now,self.height))
        
        #Angle to +y direction
        yPlusAngle = math.degrees(math.atan2(13.5-y_now,self.height))
        
        #Angle to -y direction
        yMinusAngle = math.degrees(math.atan2(-13.5-y_now,self.height))
        
        return (xPlusAngle, xMinusAngle, yPlusAngle, yMinusAngle)
    
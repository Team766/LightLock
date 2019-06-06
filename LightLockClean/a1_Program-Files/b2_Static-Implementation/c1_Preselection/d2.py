class robotPosition:
    
    def __init__(self,x_start,y_start, heading_start): #Allows location to be restarted by creating new object
        self.x_pos = x_start
        self.y_pos = y_start
        self.heading = heading_start
        
        #Add error checking at some point for x_start, y_start, heading_start out of bounds
        
        return None
    
    def updatePosition(self,x_now, y_now, heading_now): #Hard-sets new position
        self.x_pos = x_now
        self.y_pos = y_now
        self.heading = heading_now
        return 0
    
    def shiftPosition(self,x_now,y_now,heading_now): #Shifts relative to current position
        self.x_pos = self.x_pos + x_now
        self.y_pos = self.y_pos + y_now
        self.heading = self.heading + heading_now
        return 0
    
    def returnPosition(self):
        return (self.x_pos,self.y_pos,self.heading)
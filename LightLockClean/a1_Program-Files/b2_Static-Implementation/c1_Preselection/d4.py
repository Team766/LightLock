#Light Class
class Light:

    def __init__(self,x,y):
        self.x_pos = x
        self.y_pos = y
    
    def getLightPosition(self):
        return (self.x_pos,self.y_pos)
    
    def setLightPosition(self,x,y):
        self.x_pos = x
        self.y_pos = y
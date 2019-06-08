def RobotStartingPoint(TWO_CHAR_ID,ClassName):
    if TWO_CHAR_ID == "br":
        ClassName.updatePosition(1,1,1)
    elif TWO_CHAR_ID == "bc":
        ClassName.updatePosition(2,2,2)
    elif TWO_CHAR_ID == "bl":
        ClassName.updatePosition(3,3,3)
    elif TWO_CHAR_ID == "rr":
        ClassName.updatePosition(-1,-1,-1)
    elif TWO_CHAR_ID == "rc":
        ClassName.updatePosition(-2,-2,-2)
    elif TWO_CHAR_ID == "rl":
        ClassName.updatePosition(-3,-3,-3)
    else:
        return -1 #For Error Detection
    
    return ClassName.returnPosition()
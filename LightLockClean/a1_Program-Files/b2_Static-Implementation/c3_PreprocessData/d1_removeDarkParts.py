lowBound = 200
upperBound = 255

#Convert Image to display only useful lighted parts
white = cv2.inRange(testImg,lowBound,upperBound) #Strips all non-white parts of the image out. Must be tuned
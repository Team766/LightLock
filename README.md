# LightLock
Ceiling-light based localizer, generally intended for FIRST Robotics.


a0 is for documentation, math, notes, etc, and is generally underused. I should change that.
a2 is for static images, and should just be deleted. I don't need it anymore. Note: Just did that.

a1 is for program code. It is organized as thus:
  b0 is the main file. Whatever Kalman filters, redundancies, or suchlike make it onto the competition robot go in there. It maybe should...
  ...be reorganized, and maybe removed, but that is a subject for discussion.
  b1 is the dynamic implementation. It should be able to take in video and output position, so it could run on a robot, but without ...
  ...advanced features. 
  b2 is the first static implementation. It should take an image and a previously known point close by and figure out the new position. ...
  ...It has mostly been abandond due to me realising my code is a POS, and will gradually be migrated to b3.
  b3 is the better implementation of static. 
    c1_Image takes in the selected image
    c2_Process makes the image look like necessary and pulls out points, angles, ranges, etc. for ...
    c3_Extraction, which applies the actual math necessary to find the position.
    c4_Talks to output systems, like the robot, and is hardware-dependant. It is more a feature of b1
    
for b3
  c1 is simple, c2 is complicated, c3 is simple, and c4 is a print statement
  

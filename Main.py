#!/usr/bin/python
#

# @author Anand Patil
# @version January 11, 2018
# @course Programming 1
# @assign.ment Data Mining

import gliders
import turtles
import mammals

print "What would you like to do? \n Enter '1' for information about turtles. \n Enter '2' for information about gliders. \n Enter '3' for information about mammals."
i = input("Enter your number here: ")

if i == 1:
    turtles.code()
elif i == 2:
    gliders.code()
elif i == 3:
    mammals.code()
else:
    print "Please either 1, 2, or 3. \n Exiting..."
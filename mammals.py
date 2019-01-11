#!/usr/bin/python
#

# @author Anand Patil
# @version January 11, 2018
# @course Programming 1
# @assign.ment Data Mining

def code():
    file = open("data/mammals.csv", "r")
    alive = 0
    dead = 0
    numbers = []
    for line in file:
        data = line.split(",")   
        try:
            numbers.append(int(data[10]))
            if data[7] == '"N"':
                dead += 1
            elif data[7] == '"Y"':
                alive += 1
        except Exception:
            pass
    f = 0
    for i in numbers:
        f += numbers[i]
    print "Average temperature when animals were found: " + str(f / len(numbers)) + "."
    print "Mammals found alive: " + str(alive) + "."
    print "Mammals found dead: " + str(dead) + "."

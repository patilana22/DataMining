import time

def code():
    file = open("data/turtles.csv", "r")
    alive = 0
    dead = 0
    for line in file:
        data = line.split(",")
        if data[7] == '"Y"':
            alive += 1
        elif data[7] == '"N"':
            dead += 1
    print "Total number of turtles (alive and dead):", alive + dead
    print "In the file there are", alive, "turtles found alive."
    print "In the file there are", dead, "turtles found dead."
    time.sleep(1)
    print "Alive turtle to dead turtle ratio:", float(alive)/dead
    print "Percentage Alive:", (float(alive)/(alive + dead)) * 100
    print "Percentage Dead:", (float(dead)/(alive + dead)) * 100
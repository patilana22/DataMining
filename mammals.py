def code():
    file = open("data/mammals.csv", "r")
    alive = 0
    dead = 0
    numbers = []
    for line in file:
        data = line.split(",")   
        try:
            numbers.append(int(data[10]))
        except Exception:
           pass 
    f = 0
    for i in numbers:
        f += numbers[i]
    print "Average temperature when animals were found: " + str(f / numbers.__len__()) + "."

def code():
    file = open("data/mammals.csv", "r")
    alive = 0
    dead = 0
    for line in file:
        data = line.split(",")
        if data[7] == '"Y"':
            alive += 1
        elif data[7] == '"N"':
            dead += 1
    print alive, "mammals were found alive."
    print dead, "mammals were found dead."
    
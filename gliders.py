def code():
    file = open("data/gliders.csv", "r")
    numbers = []
    numbersLon = []
    numbersLat = []
    for line in file:
        data = line.split(",")    
        try:
            numbers.append(int(data[9]))
            numbersLon.append(int(data[5]))
            numbersLat.append(int(data[4]))
        except Exception:
           pass
    f = 0
    fLon = 0
    fLat = 0
    for i in numbers:
        f += numbers[i]
    for i in len(numbersLat):
        fLat += numbersLat[i]
    for i in len(numbersLon):
        fLon += numbersLon[i]
    print "Average week when animals were found: " + str(f / numbers.__len__()) + "."
    print "Average latitude where animals were found: " + str(fLat / numbersLat.__len__()) + "."
    print "Average longitude where animals were found: " + str(fLon / numbersLon.__len__()) + "."
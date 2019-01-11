def code():
    file = open("data/gliders.csv", "r")
    numbers = []
    numbersLon = []
    numbersLat = []
    numbersSal = []
    for line in file:
        data = line.split(",")    
        try:
            numbers.append(int(data[9]))
            numbersLon.append(float(data[5]))
            numbersLat.append(float(data[4]))
            numbersSal.append(float(data[11]))
        except Exception:
            pass
    f = 0
    fLon = 0
    fLat = 0
    fSal = 0
    for i in numbers:
        f += numbers[i]
    for j in range(0, len(numbersLat)):
        fLat += numbersLat[j]
    for k in range(0, len(numbersLon)):
        fLon += numbersLon[k]
    for h in range(0, len(numbersSal)):
        fSal += numbersSal[h]
        
    print "Average week when animals were found: " + str(f / len(numbers)) + "."
    print "Average latitude where animals were found: " + str(fLat / len(numbersLat)) + "."
    print "Average longitude where animals were found: " + str(fLon / len(numbersLon)) + "."
    print "Average salinity of the water where animals were found: " + str(fSal / len(numbersSal)) + "."
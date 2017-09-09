def ceiling(n):
    if isinstance(n, int):
        return int(n)
    return int(n)+1

minLat = 41.64460409
maxLat = 42.02255356

minLong = -87.92890945
maxLong = -87.61072824

width = maxLat - minLat
length = maxLong - minLong

def coordCalc(a,b):
    x = ceiling((a-minLat)/(width/100)) 
    y = ceiling((b - minLong)/(length/100))
    return 100*(x-1) + y-1
new_file = open("crime_data_new_2016.csv","w")
stringList = []
with open("crime_data_2016.csv") as file:
    lineList = file.readlines()
    for string in lineList:
        data = string.split(",")
        new = str(coordCalc(float(data[3]), float(data[4])))
        del data[4]
        del data[3]
        data.append(new)
        for string in data:
            new_file.write(string)
            new_file.write(",")
        new_file.write("\n")
new_file.close()

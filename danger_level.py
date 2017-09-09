danger = [0]*10000
with open("final_tentacle.csv") as file:
    lineList = file.readlines()
    for line in lineList:
        data = line.split(",")
        danger[int(data[3])] += 1
print(danger)

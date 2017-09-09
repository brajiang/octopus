from sklearn.neural_network import MLPClassifier

import numpy as np
crimes = ['THEFT', 'CRIMINAL DAMAGE', 'BATTERY', 'MOTOR VEHICLE THEFT', 'WEAPONS VIOLATION', 'CRIMINAL DAMAGE', 'DECEPTIVE PRACTICE', 'HOMOCIDE', 'ROBBERY', 'ARSON', 'SEX OFFENSE', 'CRIM SEXUAL ASSAULT','PUBLIC PEACE VIOLATION', 'INTERFERENCE WITH PUBLIC OFFICER', 'OFFENSE INVOLVING CHILDREN', 'ASSAULT', 'STALKING', 'KIDNAPPING', 'NARCOTICS', 'CRIMINAL', 'TRESPASS']
X = []
y = []
count=0
with open("crime_data_2016_small.csv") as file:
    lineList = file.readlines()
    for string in lineList:
        data = string.split(",")
        # init features
        xrow = []
        yrow = []
        xrow.append(float(data[0]))
        xrow.append(float(data[1]))
        xrow.append(float(data[3]))
        X.append(xrow)
        # init targets
        yrow = [0]*21
        i = crimes.index(data[2])
        yrow[i]=1
        y.append(yrow)
        count +=1 
clf = MLPClassifier(activation = 'logistic')
clf.fit(X,y)


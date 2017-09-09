from sklearn.neural_network import MLPClassifier
import pickle
import numpy as np
crimes = ['THEFT', 'CRIMINAL DAMAGE', 'BATTERY', 'MOTOR VEHICLE THEFT', 'WEAPONS VIOLATION', 'CRIMINAL DAMAGE', 'DECEPTIVE PRACTICE', 'HOMICIDE', 'ROBBERY', 'ARSON', 'SEX OFFENSE', 'CRIM SEXUAL ASSAULT','PUBLIC PEACE VIOLATION', 'INTERFERENCE WITH PUBLIC OFFICER', 'OFFENSE INVOLVING CHILDREN', 'ASSAULT', 'STALKING', 'KIDNAPPING', 'NARCOTICS', 'CRIMINAL TRESPASS', 'OTHER OFFENSE', 'BURGLARY', 'CONCEALED CARRY LICENSE VIOLATION', 'HUMAN TRAFFICKING', 'PUBLIC INDECENCY', 'PUBLIC PEACE VIOLATION', 'WEAPONS VIOLATION', 'INTIMIDATION', 'OBSCENITY']
X = []
y = []
count=0
print("running")
danger = [0]*10000
with open("final_tentacle.csv") as file:
    lineList = file.readlines()
    for line in lineList:
        data = line.split(",")
        danger[int(data[3])] += 1
with open("final_tentacle.csv") as file:
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
        yrow = [0]*29
        i = crimes.index(data[2])
        yrow[i]=1
        y.append(yrow)
        count +=1

clf = MLPClassifier(activation='tanh', tol=1e-4, warm_start='True', max_iter=1000)
clf.fit(X,y)
input("Enter latitude: ")
input("Enter longitude: ")
print("Crime risk is high")
while(True):
    answer=input('What crime? Please use all caps, single quotes and type HELP if you need a list of available queries:  ')
    if answer == 'HELP':
        print '[%s]'% ', '.join(map(str,crimes))
        continue
    else:
        break
num=crimes.index(answer)
predprob=(clf.predict_proba([[20,4,7549]]))
#predprob=(clf.predict_proba([[200,4,8549,]]))
#print(predprob)
sum=0
for i in range(0,29):
    sum=sum+predprob[0][i]

print("If a crime occurs, probability of "+str(answer)+" is "+str(predprob[0][num]/sum*100)+" percent!")
#tentacle_model=open(tentacle_model.txt,"w")
#pickle.dump(clf,tentacle_model)
#tentacle_model.close()
s=pickle.dumps(clf)
clf2=pickle.loads(s)
from sklearn.externals import joblib
joblib.dump(clf,'tentacles.pkl')

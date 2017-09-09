stringList = []
dayCount = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def convertDate(dstr):
    x = dstr.split("/")
    a = int(x[0])*10**6 + int(x[1])*10**4
    return a

def dayCounter(n):
    r = n//1000000
    s = (n//10000) % 100
    count = 0
    for i in range(r-1):
        count = count + dayCount[i]
    count = count + s
    return count

def dateCalc(dstr):
    return dayCounter(convertDate(dstr))

def timeCalc(tstr):
    lst = tstr.split(":")
    answer = int(lst[0])+int(lst[1])/60
    answer = int(answer*100) / 100
    return str(answer)

new_file = open("crime_data_new_2016.csv","w")
with open("crime_data_2016.csv") as file:
    lineList = file.readlines()
    for string in lineList:
        data = string.split(",")
        data[0] = str(dateCalc(data[0]))
        data[1] = timeCalc(data[1])
        for x in data:
            new_file.write(",")
            new_file.write(x)
        '''
        for i in range(len(string)):
            if string[i] == ',':
                break
        instr = string[:i]
        secstr = string[i:]
        stringList.append(str(dateCalc(instr)) + secstr)
        '''                
#for string in stringList:
 #   new_file.write(string)
#new_file.close()


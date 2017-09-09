timeList = [1,2,3,4,5,6,7,8]

def timeCalc(n):
    if n == 24:
        return 1
    for i in range(1,9):
        if n >= 3*(i-1) and n < 3*i:
            return str(i)

new_file = open("the_final_2016.csv","w")
    
with open("final_data_2016.csv") as file:
    lineList = file.readlines()
    for string in lineList:
        lsd = string.split(",")
        lsd[1] = timeCalc(lsd[1])
        for string in lsd:
            new_file.write(string)
            new_file.write(",")
        new_file.write("\n")
new_file.close()
        

    
        
        

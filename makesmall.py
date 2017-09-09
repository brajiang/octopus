new_file = open("smallfinal_2016.csv")

with open("the_final_2016.csv", "w"):
    lineList = file.readlines()
    for i in range(0, len(lineList)+1, 10):
        new_file.write(lineList[i])
        new_file.write('\n')

new_file.close()
    
        

timeList = [1,2,3,4,5,6,7,8]

def timeCalc(n):
    if n == 24:
        return 1
    for i in range(1,9):
        if n >= 3*(i-1) and n < 3*i:
            return i

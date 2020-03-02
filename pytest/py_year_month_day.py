import os
import sys
import time

year = int(sys.argv[1])
month = int(sys.argv[2])
day = int(sys.argv[3])
addDay = int(sys.argv[4])
nowTime = time.time()

def checkInfo():
    sign = True
    if(year<=0 or month<=0 or day<= 0):
        sign = False
    if(isLeapYear(year)):
        #闰年情况
        if(month == 2):
            if(day>29):
                sign = False
    else:
        #不是闰年
        if(month == 2):
            if(day>28):
                sign - False
    if(month>12 or day >31):
        sign = False
    return sign

def isLeapYear(checkYear):
    if(checkYear%400 == 0 or (checkYear%4 == 0 and checkYear%100 != 0)):
        return True
    return False

def main():
    changeTime = 0
    if(checkInfo() == False):
        print("输入格式有误")
        sys.exit()
    elif(addDay>=0):
        changeTime = addDay*24*60*60
    
    result = nowTime + changeTime
    return result
    
result = main()
print("{0}天后是{1}".format(addDay,time.asctime(time.localtime(result))))


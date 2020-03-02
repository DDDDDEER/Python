import xlrd
import os
import sys
import json

path = r'D:\Python\pytest'

def openExcel(path):
    workBook = xlrd.open_workbook(path)
    for sheet in workBook.sheet_names():
        sheetTemp = workBook.sheet_by_name(sheet)
        importType = str(sheetTemp.cell(0,1).value)
        configName = str(sheetTemp.cell(1,1).value)
        configHead = str(sheetTemp.cell(0,4).value)
        configTail = str(sheetTemp.cell(1,4).value)
        configKeyCount = int(sheetTemp.cell(2,1).value)
        if(importType.find('base') >= 0):
            doBase(sheetTemp,configName,configHead,configTail,configKeyCount)

def doBase(sheet:xlrd.sheet,configName:str,configHead:str,configTail:str,configKeyCount:int):

    outputTypeList = sheet.row_values(5,1,sheet.ncols)
    markList = sheet.row_values(6,1,sheet.ncols)
    clientConfig = {}
    serverConfig = []
    print("key数量:",configKeyCount)
    for i in range(configKeyCount):
        for j in range(7,sheet.nrows):
            cellValue = sheet.cell(j,i+1).value
            tempdict = {}
            if ((cellValue in clientConfig) == True):
                for k in range(1,sheet.ncols):
                    tempdict[markList[k-1]] = sheet.cell(j,k).value
                clientConfig[cellValue].append(tempdict)
            else:
                for n in range(1,sheet.ncols):
                    tempdict[markList[n-1]] = sheet.cell(j,n).value
                clientConfig[cellValue] = [tempdict]
    print("数据：",clientConfig)

def main():
    for root, dirs, files in os.walk(path):
    #walk遍历当前目录下所有子文件夹与子文件
        for filesname in files:
            if os.path.isfile(os.path.join(root,filesname)) and (str.find(filesname,'.xlsx')!=-1):
                print("find file：",os.path.join(root,filesname))
                openExcel(os.path.join(root,filesname))

main()
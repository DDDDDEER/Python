import xlrd
import os
import sys
import json
import re
import unicodedata

path = r'D:\Python\pytest'
targetPath = r'D:\Python\pytest\json'
os.chdir(path)

def openExcel(path):
    workBook = xlrd.open_workbook(path)
    for sheet in workBook.sheet_names():
        sheetTemp = workBook.sheet_by_name(sheet)
        checkSheet(sheetTemp,path)

def checkSheet(sheet:xlrd.sheet,path:str):
    if(sheet.nrows<=0 or sheet.ncols<=0):
        return
    importType = str(sheet.cell(0,1).value)
    configName = str(sheet.cell(1,1).value)
    configHead = str(sheet.cell(0,4).value)
    configTail = str(sheet.cell(1,4).value)
    configKeyCount = int(sheet.cell(2,1).value)
    if(len(importType)>0):
        if(importType.find('tiny') >= 0):
            doTiny(sheet,configName,configHead,configTail,configKeyCount)
        elif(importType.find('base') >= 0):
            doBase(sheet,configName,configHead,configTail,configKeyCount)
    else:
        print(path,"->表格数据错误")

def doTiny(sheet:xlrd.sheet,configName:str,configHead:str,configTail:str,configKeyCount:int):
    clientConfig = {}
    fileName = configHead.split("=")[0]
    for i in range(5,sheet.nrows):
        markSign = sheet.cell(i,1).value
        param = sheet.cell(i,2).value
        value = sheet.cell(i,3).value
        print("参数名字",param)
        #分析单元格数据
        if(type(value) == str):
            print("字符串数据",value)
            valueList = re.findall(r'{(.*)}',value)
            print("valueList:",valueList)
            if(len(valueList)>0):
                str1 = valueList[0]
                valueList1 = re.findall(r'{(.*?)}',str1)
                #双层括号变数组
                if(len(valueList1)>0):
                    resultList = []
                    for item in range(len(valueList1)):
                        temp = valueList1[item]
                        doubleList2 = temp.split(",")
                        resultDict = {}
                        for item2 in range(len(doubleList2)):
                            str3 = doubleList2[item2]
                            doubleList3 = str3.split("=")
                            # print(doubleList3)
                            if is_number(doubleList3[1]) == True:
                                doubleList3[1] = float(doubleList3[1])
                            resultDict[doubleList3[0]] = doubleList3[1]
                        resultList.append(resultDict)
                    # print("result:",resultList)
                    if(markSign.find("c")>=0):
                        clientConfig[param] = resultList
                #单层括号拆分
                else:
                    # print("单层括号：",str1)
                    if(str1.find("=")>=0):
                        str1List = str1.split(",")
                        resultDict = {}
                        for mark in range(len(str1List)):
                            str2 = str1List[mark]
                            str2List = str2.split("=")
                            testArray = re.findall(r'[[](.*?)[]]',str2List[0])
                            if is_number(str2List[1]) == True:
                                str2List[1] = float(str2List[1])
                            if len(testArray)>0:
                                resultDict[testArray[0]] = str2List[1]
                            else:
                                # print("str2List",str2List)
                                resultDict[str2List[0]] = str2List[1]
                        # print("result:",resultDict)
                        if(markSign.find("c")>=0):
                            clientConfig[param] = resultDict
                    else:
                        str1List = str1.split(",")
                        if len(str1List)>0:
                            resultList = []
                            resultList = str1List
                            if(markSign.find("c")>=0):
                                clientConfig[param] = resultList
                        else:
                            if(markSign.find("c")>=0):
                                if is_number(str1) == True:
                                    str1 = float(str1)
                                clientConfig[param] = str1 
            else:
                print("无大括号的数据",value)
                if(markSign.find("c")>=0):
                    clientConfig[param] = value
        else:
            print("不是字符串的数据",value)
            if(markSign.find("c")>=0):
                clientConfig[param] = value
    print("最终结果",clientConfig)
    if(len(clientConfig)>0):
        fileDict = {}
        fileDict[fileName] = clientConfig
        outputResult = json.dumps(fileDict,ensure_ascii=False)
        os.chdir(targetPath)
        file_obj = open(fileName+".json",'w',encoding="utf-8")
        file_obj.write(outputResult)
        file_obj.close()   
        
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def doBase(sheet:xlrd.sheet,configName:str,configHead:str,configTail:str,configKeyCount:int):
    return 0
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

    # #从第二列开始到Key值的位置
    # for i in range(1,configKeyCount+1):
    #     colsValue = sheet.col(i)
    #     #从第六行开始
    #     for j in range(5,sheet.nrows):
    #         tempDic = {}
    #         for k in range(len(outputTypeList)):
    #             tempDic[markList[k]] = sheet.cell(j+2,k).value
    #         if(str(outputTypeList[k]).find('c')>=0):
    #             clientConfig[colsValue[j]] = tempDic
    #         elif(str(outputTypeList[k]).find('s')>=0):
    #             serverConfig.append(tempDic)

# def jsonFactory(sheet:xlrd.sheet,keyCount:int,dics:dict = {}):
#     while (keyCount>0):
        
#         tempDict = {}
#         for i in range(7,sheet.nrows):
#             for j in range(1,sheet.ncols):
#                 tempDict[sheet.cell(keyCount,i).value] = 
#         if(len(dics)>0):
#             dics[sheet.cell(keyCount,i).value] = 
    
def main():
    for root, dirs, files in os.walk(path):
    #walk遍历当前目录下所有子文件夹与子文件
        for filesname in files:
            if os.path.isfile(os.path.join(root,filesname)) and (str.find(filesname,'.xlsx')!=-1):
                print("find file：",os.path.join(root,filesname))
                openExcel(os.path.join(root,filesname))

main()
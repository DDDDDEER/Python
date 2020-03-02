# -*- coding:utf-8 -*-
import xlrd
import os
import json

#path = os.getcwd()+r'\excel'
path = r'D:\Python\pytest'
targetPath = r'D:\Python\pytest\json'
os.chdir(path)

def readExcel(path):
    #open_workbook打开一个excel文件
    workBook = xlrd.open_workbook(path)
    #遍历所有的sheet
    for sheet in workBook.sheet_names():
        #获取sheet内容
        sheetTemp = workBook.sheet_by_name(sheet)
        result = []
        #获取行和列的数量
        rowsCount = sheetTemp.nrows
        colsCount = sheetTemp.ncols
        if rowsCount>0 and colsCount>0:
            config = sheetTemp.cell(0,0).value
            #控制循环行开始的位置
            for i in range(1,rowsCount):
                dicts = {}
                #控制循环列开始的位置
                for j in range(1,colsCount):
                    dicts[sheetTemp.cell(0,j).value] = sheetTemp.cell(i,j).value
                result.append(dicts)
        # print("表名："+str(config))
        #写入列表到文件
        os.chdir(targetPath)
        file_obj = open("{0}.json".format(str(config)),"w",encoding="utf-8")
        #json.dumps加上ensure_ascii = False解决中文出现斜杆字符
        result = json.dumps(result,ensure_ascii=False)
        file_obj.write(str(result))

for root, dirs, files in os.walk(os.getcwd()):
    #walk遍历当前目录下所有子文件夹与子文件
    for filesname in files:
        if os.path.isfile(os.path.join(root,filesname)) and (str.find(filesname,'.xlsx')!=-1):
            print("find file：",os.path.join(root,filesname))
            readExcel(os.path.join(root,filesname))
    
# -*- coding:utf-8 -*-
import xlrd
import os
import json

#path = os.getcwd()+r'\excel'
path = r'D:\software\BaiduDiskData\农场项目\N-农场项目\数据表'
os.chdir(path)

def readExcel(path):
    workBook = xlrd.open_workbook(path)
    print("sheetName:",workBook.sheet_names())
    for sheet in workBook.sheet_names():
        sheetTemp = workBook.sheet_by_name(sheet)
        print("rowsCount:",sheetTemp.nrows)
        print("colsCount:",sheetTemp.ncols)
        result = []
        rowsCount = sheetTemp.nrows
        colsCount = sheetTemp.ncols
        if rowsCount>0 and colsCount>0:
            config = sheetTemp.cell(0,0).value
            for i in range(5,rowsCount):
                dicts = {}
                for j in range(1,colsCount):
                    dicts[sheetTemp.cell(0,j).value] = sheetTemp.cell(i,j).value
                result.append(dicts)
        print("表名："+str(config))
        
        for item in result:
            print(json.dumps(item,ensure_ascii=False))


for files in os.listdir():
    if os.path.isfile(files) and files.find('.xlsx'):
        readExcel(os.path.join(path,files))
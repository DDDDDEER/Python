# -*- coding:utf-8 -*-
#os模块的使用
import os

path = os.getcwd()
print('当前工作目录：%s'%path)
searchDir = path + "\\test"
print("切换后工作目录"+searchDir)

os.chdir(searchDir)

file_obj = open("test.txt","r",encoding = "utf-8")
for line in file_obj.readlines():
	print(line)

file_obj.close()
	
	
	

	

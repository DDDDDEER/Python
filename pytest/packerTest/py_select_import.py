# -*- coding:utf-8 -*-
import os
import re

findPattern = re.compile(r'^import')

writePath = os.getcwd()+"\\test"
print("当前目录:"+writePath)

searchPath = "D:\SVNdata"

importList = []

def writeFile(line):
	global writePath
	if(len(line)>0):
		os.chdir(writePath)
		file_obj = open("test.txt","a+",encoding = "utf-8")
		file_obj.write(line)
		file_obj.close()

def readFile(file_name,path):
	global findPattern
	global importList
	if not os.path.isdir(path):
		print("路径错误:"+path)
		return
	os.chdir(path)
	file_obj = open(file_name,"r",encoding = "utf-8")
	for line in file_obj.readlines():
		if(findPattern.match(line) != None):
			temp = line.replace('/n',"")
			temp = temp.replace('/r',"")
			temp = temp.replace(' ',"")
			if(temp not in importList):
				importList.append(temp)
				writeFile(line)
	file_obj.close()

for root,dirs,files in os.walk(searchPath):
	for fileItem in files:
		if(fileItem.find(".py")>=0):
			print("reading-------------------"+os.path.join(root,fileItem))
			readFile(fileItem,root)



# -*- coding:utf-8 -*-
import os
import sys

path = os.getcwd()
findPath = "D:\SVNdata"
#print(path)
#workDir = os.path.dirname(__file__)
#print(os.path.join(workDir,"test"))
if(os.path.isdir(path+"\\test")):
	print("目录已存在")
else:
	os.mkdir("test")
	print("创建新目录")

os.chdir(path+"\\test")
testFile = open("test.txt","w",encoding = "utf-8")

#os.walk()返回一个三元组格式的数据
for root,dirs,files in os.walk(findPath):
	#print("\n")
	#print("root:%s"%root)
	#print("dirs:%s"%dirs)
	#print("files:%s"%files)
	for fileItem in files:
		#文件名
		#print("fileItem1:%s"%fileItem)
		if(fileItem.find(".py")>=0):
			testFile.write(os.path.join(root, fileItem)+"\n")
			print("write--------------------"+fileItem)
		#加上路径
		#print("fileItem2:%s"%os.path.join(root, fileItem))
testFile.close()
		
	

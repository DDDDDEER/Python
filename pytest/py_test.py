
import os
import sys
import json
import train

params_list = []


file_obj = open("test.txt","r",encoding = "utf-8")
for line in file_obj.readlines():
    params_list.append(json.loads(line))
file_obj.close()

if len(params_list)>0:
    for param in params_list:
        train_obj = train(param)
        train_obj.run()
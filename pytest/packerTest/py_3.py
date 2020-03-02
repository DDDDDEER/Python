param = 5
#迭代方法执行斐波那契
def func1(x):
	a1 = 1
	a2 = 1
	a3 = 1
	if(x < 1):
		return 0
	elif(x == 1 or x == 2):
		return 1
	else:
		while(x-2)>0:
			a3 = a1 + a2
			a1 = a2
			a2 = a3
			x = x-1
		return a3

result = func1(param)
print("迭代结果为%d"%result)
#递归方法执行斐波那契
def func2(x):
	if x<1:
		return 0
	elif x==1 or x==2:
		return 1
	else :
		return func2(x-1)+func2(x-2)

result2 = func2(param)
print("递归结果为%d"%result2)


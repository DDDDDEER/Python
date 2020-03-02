import random
temp = input("input a number:")
guess = int(temp)
anser = random.randint(1,100)
testcount = 10
while (guess != anser):
	if guess < anser:
		print("input small than result")
	else:
		print("input big than result")
	testcount -= 1
	print("testcount:",testcount)
	temp = input("input a number:")
	guess = int(temp)
	
	if testcount <= 0:
		print("count < 0 game over!")
		break
if (guess == anser):
    print("sucess!")


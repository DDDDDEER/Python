print("A:90-100,B:80-90,C:60-80,D:0-60")
score = int(input("input a score to test!\n"))
if score <0 or score >100:
    print("err input,please input again!")
    score = int(input("input a score to test!\n"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 60 <= score < 80:
    print("C")
elif score < 60:
    print("D")
else:
	print("err input")

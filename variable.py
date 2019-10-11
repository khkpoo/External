a=[1,2,3]
b=a

if (id(a) == id(b)):					# 변수는 주소가 공유된다 (대입아닙)
	print("a :",id(a)," b :",id(b))
else:
	print("else")
a.append(4)
print(a)
print(b) 
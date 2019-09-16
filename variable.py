a=[1,2,3]
b=a
if (id(a) != id(b)):
	print("a :",id(a)," b :",id(b))
else:
	print("else")
a.append(4)
print(a)
print(b) 
# List
## List 기본 사용법
l1=[]
l2=[1,2,3,2]
l3=[1,"str",[1,2]]
print(len(l2))
print(type(int(str(l2[0]))))

print(l3[-1][1],type(l3[-1]),type(l3[-1][1]))	# -1은 마지막값. 이중 인덱스값사용가능
print(l3[1],type(l3[1]))
print('{0:=^100}'.format("end"))

## List 연산
print(l2+l3)		# Append
print(l2*2)			# 반복
print(l2.count(3))

print(len(l3))

print('{0:=^100}'.format("end"))


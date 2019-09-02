# List
## List 기본 사용법
l1=[]
l2=[1,2,3,2]
l3=[1,"str",[1,2]]
l4=[4,5,6,7]
print(len(l2))
print(type(int(str(l2[0]))))
print(l3[-1][1],type(l3[-1]),type(l3[-1][1]))	# -1은 마지막값. 이중 인덱스값사용가능
print(l3[1],type(l3[1]))
print('{0:=^100}'.format("end"))

## List 연산
print("확장")
print(l2+l3)						# 확장
l4.extend(l3)
print(l4)

print(l2*2)							# 반복
print(l2.count(3))					# 포함 요소 검색
print(len(l3))						# 요소 개수 확인
print('{0:=^100}'.format("end"))

## List 요소
print(l2)
l2.append(100)				# "값"을 추가
print(l2)
l2.insert(4, 400)			# arg1 위치에 arg2"값""을 추가
print(l2)
l2.remove(2)				# "값"을 제거 중복되면 첫번재꺼지움
print(l2)
del(l2[3])					# 지정 요소 삭제
print(l2)
l2.sort()					# 정렬
print(l2)
l2.sort(reverse=True)
print(l2)
print(l2.pop())				# 기본 (마지막)요소 꺼내기 (꺼내서 리턴후 삭제)
print(l2)
print(l2.pop(0))			# 선택한 요소 꺼내기
print(l2)

print('{0:=^100}'.format("end"))

## Tuple 기본 사용법
### List와 달리 ()
### 삭제 수정이 불가능
### 한개요소만 가질때 (1,) 이런식으로 뒤에 콤마를써줘야함
### ()를 생략해도 됨

## Dictionary
### { }
### Key : Value
### Key 는 유니크해야하며 Lis자료형을 쓸수없다
person = {'name' : 'A', 'number' : 1}
people = []
print('{0:=^100}'.format("end"))
for i in range(0, 10):	
	print(i)
	person['number'] = i
	print(people)
	people.append(person)

print(people)	
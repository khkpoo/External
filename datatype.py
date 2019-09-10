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
print('{0:=^100}'.format(" start "))
print(person.keys())		# Key 값 알아오기 리턴타입은 dict_keys
for i in person.keys():
	print(i)
print(list(person.keys()))	# Key 값 list형태로 벼환
print(person.values())		# Value 값 알아오기 리턴타입은 dict_values
for i in person.values():
	print(i)
print(person.items())		# Item(Key Value 쌍 리턴. dict_items
for i in person.items():
	print(i)
print(person['name'])		# 값 가져오기
print(person.get('name'))
print(person.get('name3','Default Value'))	# 값없을 경우 NVL처리
print('name' in person)		# Key 존재여부
print('name3' in person)
person.clear()				# Dictionary Clear

## Set 집합연산자
### 중복허용하지 않음
### 순서 없음
s1=set("HELLo")
s2=set(['w','o','r','l','d'])
print(s1)
print(s2)
print(s1 & s2)				# 교집합 
print(s1.intersection(s2))
print(s1 | s2)				# 합집합
print(s1.union(s2))
print(s1-s2)				# 차집합
print(s1.difference(s2))
s1.add('r')					# 요소 추가
print(s1)
s1.update('ABCDH')			# 요소들 추가
print(s1)
s1.remove('A')				# 요소 제거
print(s1)
print('{0:=^100}'.format(" END "))

## Bool
### True / False
list = [1,2,3,4]
while list:
	print(list.pop())
	
print(bool("Exists"))
print(bool(""))
#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

str1="Hello Python!"

# 문자열 포메팅
print("{0}과 {1}".format('left','right'))	# 인자 사용하기
print("{0:>100}".format("right"))			# 오른쪽 정렬
print("{0:<100}".format("left"))			# 왼쪽 정렬
print("{0:^100}".format("Center"))			# 가운데 정렬
print("{0:=^100}".format(" Center "))		# 빈칸 채우기
print(f'{"hi":-^100}')						# 동일 표현 (f 이용)
print(f"{'hi':-^100}")						# 동일 표현 (f 이용)
print(f'{str1}')							# 3.6~ 가능 변수참조용

print("{0}".format('*') * 100 )


# 문자열 함수
## 패턴
print(str1.count('o'))  # 패턴 개수 리턴
print(str1.find('o'))   # 패턴 위치 리턴(최초), 없을경우 -1
print(str1.index('o'))  # 패턴 위치 리턴(최초), 없을경우 에러
print("*"*100)

## 삽입
print(str1.join('abc'))	# 후행 값 중간중간에 문자열 삽입. 
print(".".join(str1))	# 이따위로 더 쓰는듯
print("*"*100)

## 대소문자
print(str1.upper())		# 대문자 어규먼트없음
print(str1.lower())		# 소문자 어규먼트없음
print("*"*100)

## 변형
str2= "  BLINK  "
print(str2.lstrip())	# 공백 제거 (왼쪽 오른쪽 모두)
print(str2.rstrip())
print(str2.strip())
print("*"*100)

## 치환
print(str1.replace("!","?"))	# 문자열 replace
print(str1.split("P"))				# 문자열 Split 하여 List로 반환
print(str2.split())
print("*"*100)

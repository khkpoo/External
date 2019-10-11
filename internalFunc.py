#Internal Function
print ( abs(-10.5) )		## 절대값

                            ## 반복가능형 자료형 (Iterable) : dict, tuple, list, str, set 
print(all([1,2]))           ## 모두 참이면 True 하나라도 거짓이 있으면 False
print(all([1,2,0]))

print(any([1,2]))           ## 하나라도 참이 있으면 True 모두 거짓이면 False
print(any([1,2,0]))

a=('A',1,'B','c','DD')      ## 순서를 갖는 오브젝트(tuple,list,str) 를 입력값으로 받아 인덱스값을 포함하는 값을 리턴
for i in a:
    print(i)

for i in enumerate(a):
    print(i)

print(dict(enumerate(a)))

## eval 실행가능한 문자열을 입력받아 실행한 결과값을 돌려줌
## len
## int
## str
## hex
## list
## tuple
## type

## chr
## ord

## dir
## divmod
## pow
## max
## min
## sum
## sorted
## round
## zip

## range
## filter
## map

## input
## open
## id
## isinstance





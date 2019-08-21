import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 문자열 함수
str1="Hello Python!"
print(str1.count('o'))  # 패턴 개수 리턴
print(str1.find('o'))   # 패턴 위치 리턴(최초), 없을경우 -1
print(str1.index('o'))  # 패턴 위치 리턴(최초), 없을경우 에러
print(str1.join('abc'))

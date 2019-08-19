import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

a="gksrmf한글을 ' '   ''' '포함한 문자열입니다"
liner="="*200
b=[]
c=''
print(liner)
for i in range(0,100,1):
    b.append(i)
    c+=str(i)

print(b[2:6])
print(c)
print(c[:4])
print(type(a)," : ",a)
print(liner[4:10])

print(liner)

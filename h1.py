import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

a="gksrmf한글을 ' '   ''' '포함한 문자열입니다"
# print(a)
# print(a[:6]+'-'+a[6:])
b=20

print("{0} is deliciaos {1}".format(b,1))
print("{0:!^100}".format(" khkpoo booofdsfs       dsfsdfsd "))
print(f"{a}")

#Internal Function
## sys 명령행 인수 전달
    ##  사용자 모듈 경로설정

# lambda x: return x>0,[1,-1]
import random
nums=list(range(1,46))
# print(random.randrange(1,45))
# pick=[]
# for i in range(45):
#     idx=random.randrange(0,45-i)
#     pick.append(nums.pop(idx))
    # print(idx)
    # nums[idx]
    # pick.append(random.randrange(1,45-i+1))
    # print(nums[random.randrange(0,45-i)])
    # nums.pop(random.randrange(0,45-))
    # print(p)
    # pass
# print(sorted(pick))

test=[]
for i in range(1000):
    test.append(random.randrange(0,45))

print(min(test) ,max(test))
print(min(nums),max(nums))



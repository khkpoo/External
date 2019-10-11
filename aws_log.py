import os
import json
region=input("Region : ")
instanceId=input("Instance Identifier : ")

# cmd1="aws rds describe-db-log-files --db-instance-identifier awspublicpg11 --region ap-northeast-2 --output json"
cmd1="aws rds describe-db-log-files --db-instance-identifier "+instanceId+" --region "+region+" --output json"
print(cmd1)

# print(type(json.loads(os.popen(cmd1).read())))
lists=json.loads(os.popen(cmd1).read())["DescribeDBLogFiles"]
files=[]
for content in lists:
    # content["LogFileName"]
    files.append(content["LogFileName"]) 
    # print(type(content["LogFileName"]))
# files.sort(reverse=True)
files.sort()

# print(type(files))

for file in files:
    print(file)
    if file:
        cmd2="aws rds download-db-log-file-portion --db-instance-identifier "+instanceId+" --region "+region+" --log-file-name "+file+" --output text >> postgresql.log" 
        print(cmd2)
        # 실제 수행하려면 아래 주석 제거
        # os.system(cmd2)
    elif not file:
        print("None Data")
    
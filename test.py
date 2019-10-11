import os
import json
import tkinter as tk
cmd1="aws rds describe-db-log-files --db-instance-identifier awspublicpg10 --region ap-northeast-2 --output json"
cmd2="aws rds download-db-log-file-portion --db-instance-identifier awspublicpg10 --region ap-northeast-2 --log-file-name error/postgres.log --output text"

class Calc:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def setValue(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b

class CalcAdvance(Calc):
    def pow(self):
        return self.a ** self.b

a=CalcAdvance()
print(a.a)
print(a.b)
a.setValue(3,3)
print(a.pow())

# a=Calc()
# a.setValue(4,5)
# print(a.add())
# print(a.sub())
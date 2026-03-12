class Bank:
 def __init__(self):
  self.a={"1001":5000,"1002":3000}
 def transfer(self,s,d,m):
  if s not in self.a or d not in self.a:raise Exception
  if self.a[s]<m:raise Exception
  self.a[s]-=m
  self.a[d]+=m
  print(self.a)

b=Bank()
try:
 s=input()
 d=input()
 m=int(input())
 b.transfer(s,d,m)
except:
 print("transaction error")
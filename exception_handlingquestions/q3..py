class Shop:
 def __init__(self):
  self.s={"shirt":10,"shoes":5}
 def order(self,p,q,c):
  if p not in self.s:raise Exception
  if self.s[p]<q:raise Exception
  if c!="SAVE10":raise Exception
  self.s[p]-=q
  print("order placed")

x=Shop()
try:
 p=input()
 q=int(input())
 c=input()
 x.order(p,q,c)
except:
 print("order error")
class Store:
 def __init__(self):
  self.p={"pen":5,"book":0}
 def buy(self,n):
  if n not in self.p:
   print("invalid product")
  elif self.p[n]==0:
   print("out of stock")
  else:
   self.p[n]-=1
   print("item sold")

s=Store()
try:
 n=input()
 s.buy(n)
except:
 print("error")
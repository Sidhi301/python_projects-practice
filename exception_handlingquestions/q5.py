class Flight:
 def __init__(self):
  self.seats=5
 def book(self,n,s):
  if n=="" :raise Exception
  if s>self.seats:raise Exception
  self.seats-=s
  print("booked")

f=Flight()
try:
 n=input()
 s=int(input())
 f.book(n,s)
except:
 print("booking failed")
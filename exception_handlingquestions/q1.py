class Contact:
 def __init__(self):
  self.c={}
 def add(self,n,p):
  if n in self.c:raise Exception
  if not p.isdigit():raise Exception
  self.c[n]=p
 def edit(self,n,p):
  self.c[n]=p
 def search(self,n):
  print(self.c[n])

b=Contact()
while True:
 print("1 add 2 edit 3 search 4 exit")
 x=input()
 try:
  if x=="1":
   n=input()
   p=input()
   b.add(n,p)
  elif x=="2":
   n=input()
   p=input()
   b.edit(n,p)
  elif x=="3":
   n=input()
   b.search(n)
  else:
   break
 except:
  print("error")
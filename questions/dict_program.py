n=int(input("enter the number of students:"))
d={}
for i in range(n):
    name=input("enter the name of the studnet:")
    marks=int(input("enter the marks of the student:"))
    d[name]=marks
    
maximum=max(d.values())
topper={name for name in d if d[name]== maximum}
print("the topper is:",topper,"with marks:",maximum)
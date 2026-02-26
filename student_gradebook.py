grade_book={}
def add_student(name,grade):
    grade_book[name]=grade
    print(f"Student {name} added with grade {grade}.")

def remove_student(name):
    if name in grade_book:
        del grade_book[name]
        print(f"Student {name} removed from the grade book.")
    else:
        print(f"Student {name} not found in the grade book.")

def view_students():
    if grade_book:
        print("Grade Book:")
        for name, grade in grade_book.items():
            print(f"{name}: {grade}")
    else:
        print("No students in the grade book.")



while True:
    print("1.add student")
    print("2.remove student")
    print("3.view students")
    print("exit")
    choice=int(input("Enter the choice: "))
    if choice==1:
        name=input("enter the name of the student:")
        grade=int(input("enter the grade of the student:"))
        add_student(name,grade)
    elif choice==2:
        name=input("enter the name of the student:")
        remove_student(name)
    elif choice==3:
        view_students()
    elif choice==4:
        print("Exiting the program.")
        break
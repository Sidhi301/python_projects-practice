registered_students = set()
rejected_students = set()

name = input("Enter your name: ")

if name in registered_students:
    print("Already registered")

elif name in rejected_students:
    print("Already rejected")

else:
    choice = input("Enter status register/reject: ")

    if choice == "register":
        registered_students.add(name)
        print("You are registered successfully")

    elif choice == "reject":
        rejected_students.add(name)
        print("You are rejected")

    else:
        print("Invalid choice")

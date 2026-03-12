try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    div=a/b
except (ValueError,ZeroDivisionError) as e:
    print(f"error occured {e}")

    

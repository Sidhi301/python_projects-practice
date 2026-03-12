class fiveDivisionError(Exception):
    pass
try:
    n1=int(input())
    n2=int(input())
    if n2==5:
        raise fiveDivisionError
    print(n1/n2)
except (fiveDivisionError,ZeroDivisionError)as e:
    print(e)

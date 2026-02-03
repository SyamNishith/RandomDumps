#d=int(input("enter a value:"))

try:
    print("RESOURCE OPENED:")
    a = int(input("enter the first value:"))
    b = int(input("enter the second value:"))
    c = a / b
    print(c)
    d=int(input("enter a value:"))
except ZeroDivisionError as e:
    print("ERROR:",e)
except ValueError as e:
    print("invalid input:",e)
except Exception as e:
    print("something went wrong:")
finally:
    print("RESOURCE CLOSED:")
class EceError(Exception):
    pass
try:
    branch=input("enter the string:")
    if branch!="ece":
        raise EceError
    
except EceError:
    print("outsiders are not allowed:")
else:
    print("welcome to ece")
finally:
    print("byee -byee")

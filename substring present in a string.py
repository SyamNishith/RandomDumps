string=input("enter the string:")
substring=input("enter the substring:")
def present(string,substring):
        if string.find(substring)==-1:
            print("no substring found")
        else:
            print("substring found in string")
present(string, substring)
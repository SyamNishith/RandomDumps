stack=[]
def push():
    if len(stack)==n:
        print("stack is full")
    else:
        elements=int(input("enter the elements:"))
        stack.append(elements)
        print(stack)
def pop():
    if not stack:
        print("stack is empty:")
    else:
        e=stack.pop()
        print("removed element is:",e)
        print(stack)
n=int(input("enter the size of stack:"))
while True:
    print("For StackOperations enter 1:push 2:pop 3:quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter correct choice for StackOperations")


queue=[]
def enqueue():
    elements=int(input("enter the elements:"))
    queue.append(elements)
def dequeue():
    if not queue:
        print("queue is empty:")
    else:
        e=queue.pop(0)
        print(e,"is removed from queue:")
def display():
    print(queue)
while True:
    print("For Queue Operations 1:Enqueue 2:Dequeue 3:display 4:quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter Correct Choice:")
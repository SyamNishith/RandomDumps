class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack_Structure:
    def __init__(self):
        self.head=None
    def push_node(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            self.head=new_node.next
            self.head=new_node
    def pop_node(self):
        if self.head==None:
            print("Stack is Empty!!No node to delete")
        else:
            deleted_node=self.head.data
            self.head=self.head.next
            return deleted_node
    def display(self):
        if self.head ==None:
            print("stack is empty!!no node to display")
        else:
            print(self.head.data)
Silly=Stack_Structure()
while True:
    print("push<value>") 
    print("pop")
    print("display")
    print("quit")
    my_input=input("choose your desired operation?:").split()
    choice=my_input[0].strip().lower()
    if choice=="push":
        Silly.push_node(int(my_input[1]))
    elif choice=="pop":
        deleted_node=Silly.pop_node()
        if deleted_node is None:
            print("stack is empty:")
        else:
            print("deleted node is:",int(deleted_node))
    elif choice=="display":
        Silly.display()
    elif choice=="quit":
        break

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def print_Sll(self):
        if self.head is None:
            print("SinglyLinkedList is Empty:")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
            if self.head is None:
                print("SLL IS EMPTY!!")
                return
            if self.head.data==x:
                new_node=Node(data)
                new_node.ref=self.head
                self.head=new_node
                return
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found")
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node
    def add_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("SLL is not empty!!")
    def delete_begin(self):
        if self.head is None:
            print("SLL IS EMPTY!!")
        else:
            self.head=self.head.ref
    def delete_last(self):
        if self.head is None:
            print("SLL IS EMPTY!!")
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.ref is None:
                    break
                n=n.ref
            if n.ref is None:
                print("Node is not present")
            else:
                n.ref=None
    def delete_value(self,x):
        if self.head is None:
            print("SLL IS EMPTY!!")
            return
        if self.head.data==x:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present:")
        else:
            n.ref=n.ref.ref
    def replace_max(self,value):
        n=self.head
        max=n
        while n!=None:
            if n.data>max.data:
                max=n
            n=n.ref
        max.data=value
    def replace_min(self,value):
        n=self.head
        min=n
        while n!=None:
            if n.data<min.data:
                min=n
            n=n.ref
        min.data=value
    def reverse_linkedlist(self):
        print()
        prev_node=None
        curr_node=self.head
        while curr_node!=None:
            next_node=curr_node.ref
            curr_node.ref=prev_node
            prev_node=curr_node
            curr_node=next_node
        self.head=prev_node
    def middlenode(self):
        slow=self.head
        fast=self.head
        while fast and fast.ref !=None:
            slow=slow.ref
            fast=fast.ref.ref
        return slow
SLL=SinglyLinkedList()
SLL.add_begin(10)
SLL.add_last(20)
SLL.add_last(30)
SLL.add_last(40)
SLL.add_after(50,40)
SLL.replace_max(56)
mid=SLL.middlenode()
print("middle node is:",mid.data)
SLL.print_Sll()

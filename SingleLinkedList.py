'''class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def Traversal(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
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
        new_node=Node(data)
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n.data is None:
            print("Node is not found")
        else:
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("Add_Before is not possible")
        elif self.head.data==x:
            new_node.ref=self.head
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                else:
                    n=n.ref
            if n.ref.data is None:
                print("Node not found")
            else:
                new_node.ref=n.ref
                n.ref=new_node
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty cannot perform deletion operation")
        else:
            self.head=self.head.ref
    def delete_last(self):
        n=self.head
        if self.head is None:
            print("linked list is empty cannot perform deletion operation")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_node(self,x):
        if self.head is None:
            print("Linkedlist is empy cannot perform deletion operation")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found")
            else:
                n.ref=n.ref.ref
    def max(self):
        n=self.head
        max=self.head.data
        while n is not None:
            if n.data > max:
                max=n.data
            n=n.ref
        return max
    def min(self):
        n=self.head
        min=self.head.data
        while n is not None:
            if n.data < min:
                min=n.data
            n=n.ref
        return min
ll=Linkedlist()
ll.add_begin(10)
ll.add_last(20)
ll.add_last(30)
ll.add_after(15,10)
ll.add_before(25,30)
a=ll.max()
print("max node is:",a)
b=ll.min()
print("min node is:",b)
ll.Traversal()'''
class StackImplementation:
    def __init__(self):
        self.listt=[]
        print("this is stack implementation")
    def push(self,value):
        self.listt.append(value)
    def pop(self):
        if self.listtt==[]:
            print("stack is empty cannot perform pop operation")
        else:
            return self.listt.pop()
    def display(self):
        if self.listt==[]:
            print("stack is empty")
        else:
            print(self.listt)
    def peek(self):
        return self.listt[-1]
    def isEmpty(self):
        if self.listt==[]:
            return True
        return False
s=StackImplementation()
s.push(10)
s.push(20)
s.push(30)
h=s.peek()
print(h)
s.display()
print(s.isEmpty())

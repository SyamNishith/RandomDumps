import collections
stack= collections.deque() # from collections module using deque class
stack.append(10)# to add elements to the stack
stack.append(20)
stack.append(30)
print(stack)
stack.pop() #to remove elements from the stack
stack.pop()
stack.pop()
print(stack)
if not stack:#returns true if stack is empty
    print("Stack is empty:")
else:
    print("stack is not empty")
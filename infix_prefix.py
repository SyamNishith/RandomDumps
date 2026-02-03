def reverse(infix_expression):
    rev=" "
    for i in infix_expression:
        if i=="(":
            i=")"
        elif i==")":
            i="("
        rev=i+rev
    return rev
def infixtoprefix(rev_infix_expression):
    stack=[]
    output=" "
    operator=set(["+","-","*","/","(",")","^"])
    priority={"+":1,"-":1,"*":2,"/":2,"^":3}
    for ch in rev_infix_expression:
        if ch not in operator:
            output=output+ch
        elif ch =="(":
            stack.append(ch)
        elif ch==")":
            while stack and stack[-1]!="(":
                output=output+stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!="(" and priority[ch]<priority[stack[-1]]:
                output=output+stack.pop()
            stack.append(ch)
    while stack:
        output=output+stack.pop()
    return output
infix_expression=input("enter your expression:")
print("Infix_Expression is:",infix_expression)
rev_infix_expression=reverse(infix_expression)
print("rev_infix_expression:",rev_infix_expression)
output=infixtoprefix(rev_infix_expression)
print("prefix exression is:",reverse(output))


def infix_postfix(string):
    stack=[]
    expression=" "
    operators=set(["+","-","*","/","^","(",")"])
    priority={"+":1,"-":1,"*":2,"/":2,"^":3}
    for character in string:
        if character not in operators:
            expression=expression+character
        elif character =="(":
            stack.append(character)
        elif character==")":
            while stack and stack[-1]!="(":
                expression=expression+stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!="(" and priority[character]<=priority[stack[-1]]:
                expression=expression+stack.pop()
            stack.append(character)
    while stack:
        expression=expression+stack.pop()
    return expression
string="m*n+(p-q)+r"
print(infix_postfix(string))


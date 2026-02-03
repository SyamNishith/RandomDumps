def balanced_paranthesis(expression):
    stack=[]
    for char in expression:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            if not stack:
                return False
            curr_char=stack.pop()
            if curr_char=="(":
                if char!=")":
                    return False
            elif curr_char=="{":
                if char!="}":
                    return False
            elif curr_char=="[":
                if char!="]":
                    return False
    if stack:
        return False
    return True
expression="[{}{}(]"
if balanced_paranthesis(expression):
    print(expression,"is a balanced paranthesis:")
else:
    print(expression,"is not balanced paranthesis")
























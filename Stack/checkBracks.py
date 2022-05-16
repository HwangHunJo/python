stack = []

def isEmpty():
    if(len(stack) == 0):
        return True
    return False

def push(e):
    stack.append(e)

def pop():
    return stack.pop()

def peek():
    if(not(isEmpty)):
        return stack[-1]
    else:
        return False

def size():
    return len(stack)

def clear():
    stack.clear()

def checkBracks(statement):
    open = ['(', '[', '{']
    close = [')', ']', '}']

    for ch in statement:
        if(ch in open):
            push(ch)
        elif(ch in close):
            if(isEmpty()):
                return False
            else:
                delete = pop()
                print(size() - 1)
                if(open.index(delete) != close.index(ch)):
                    return False
    if(isEmpty()):
        return True

str = ("[A+B]", "[C+D]]", "}[A*C]-{B/E}")
for s in str:
    result = checkBracks(s)
    print(s, "--->", result)


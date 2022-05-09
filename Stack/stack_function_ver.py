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




while(True):
    op = input("실행할 연산을 입력하시오.(isEmpty, push, pop, peek, size, clear)\n")
    if(op == "isEmpty"):
        print(isEmpty())
    
    elif(op == "push"):
        num = int(input("push할 숫자를 입력하시오.\n"))
        push(num)

    elif(op == "pop"):
        print(pop())

    elif(op == "peek"):
        print(peek())

    elif(op == "size"):
        print(size())

    elif(op == "clear"):
        clear()

    else:
        print("잘못된 연산입니다.")

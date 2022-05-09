class Stack:
    def __init__(self):
            self.data = []

    def isEmpty(self):
        if(len(self.data) == 0):
            return True
        return False

    def push(self, e):
        self.data.append(e)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if(not(self.isEmpty())):
            return self.data[-1]
        else:
            return False

    def size(self):
        return len(self.data)

    def clear(self):
        self.data.clear()



s = Stack()


while(True):
    op = input("실행할 연산을 입력하시오.(isEmpty, push, pop, peek, size, clear)\n")
    if(op == "isEmpty"):
        print(s.isEmpty())
    
    elif(op == "push"):
        num = int(input("push할 숫자를 입력하시오.\n"))
        s.push(num)

    elif(op == "pop"):
        print(s.pop())

    elif(op == "peek"):
        print(s.peek())

    elif(op == "size"):
        print(s.size())

    elif(op == "clear"):
        s.clear()

    else:
        print("잘못된 연산입니다.")

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

def evalPostfix(oper):
    s = Stack()
    for ch in oper:
        if ch in "*/+-":
            n2 = s.pop()
            n1 = s.pop()
            if ch == '*':
                s.push(n1 * n2)
            elif ch == '/':
                s.push(n1 / n2)
            elif ch == '+':
                s.push(n1 + n2)
            elif ch == '-':
                s.push(n1 - n2)
        else:
            s.push(int(ch))

    return s.pop()

expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']

print(expr1, ' --> ', evalPostfix(expr1))
print(expr2, ' --> ', evalPostfix(expr2))
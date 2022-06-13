def Queue():
    global queue
    queue  = []

def isEmpty():
    if len(queue) == 0:
        return True
    else:
        return False

def enqueue(item):
    queue.append(item)

def dequeue():
    if not isEmpty():
        return queue.pop(0)

def peek():
    if not isEmpty():
        return queue[0]

def size():
    return len(queue)

def clear():
    queue.clear()

Queue()
print("큐가 비어있나요? %s" %isEmpty())

for i in range(4):
    enqueue(10 + i)

for _ in range(2):
    print("삭제한 값은? ", dequeue())
    
print(queue)


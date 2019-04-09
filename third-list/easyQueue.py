from sys import stdin, stdout
class Node:
    def __init__(self,val):
        self.value = val
        self.next = None # the pointer initially points to nothing
        self.previous = None

head = None
tail = None
length = 0

def insert(value):
    global head
    global tail
    global length
    node = Node(value)
    if head == None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node 
    length += 1

def pop():
    global head
    global tail
    global length
    if length > 1:
        head = head.next
        length -= 1
    elif length == 1:
        head = None
        tail = None
        length -= 1
        

def operate(i):
    op = i[0]
    if op == "1":
        insert(i[1])
    elif op == "2":
        pop()
    else:
        if length > 0:
            stdout.write(head.value + "\n")
        else:
            stdout.write("Empty!\n") 

n = int(stdin.readline())
queries = [stdin.readline().split() for x in range(n)]
for query in queries:
    operate(query)
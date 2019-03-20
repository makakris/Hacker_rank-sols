class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
         return self.stack==[]
s1=Stack()
a="12+3*4-5/"
for i in a:
    if i in "0123456789":
        s1.push(int(i))
    else:
        if i=="+":
            s1.push(s1.pop() + s1.pop())
        elif i=="-":
            s1.push(s1.pop() - s1.pop())
        elif i=="*":
            s1.push(s1.pop() * s1.pop())
        elif i=="/":
            s1.push(s1.pop() / s1.pop())
        else:
            print("Invalid Operator")
print(s1.stack)
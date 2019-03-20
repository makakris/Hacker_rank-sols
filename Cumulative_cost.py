class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def pull(self):
        return self.stack[len(self.stack)-1]
s1=Stack()
a=[4,3,2,6]
a.sort()
if len(a)<=2:
    print(sum(a))
else:
    s1.push(a[0]+a[1])
    for i in range(2,len(a)):
        s1.push(s1.pull()+a[i])
print(sum(s1.stack))

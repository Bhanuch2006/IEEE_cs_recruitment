class mystack:
    def __init__(self):
        self.stack=[]
        self.stack_min=[]
        self.stack_max=[]
    def push(self,x):
        self.stack.append(x)
        if not self.stack_min or x<=self.stack_min[-1]:
            self.stack_min.append(x)
        if not self.stack_max or x>=self.stack_max[-1]:
            self.stack_max.append(x)
    def pop(self):
        if not self.stack:
            print("Cannot pop from an empty Stack")
        p=self.stack.pop()
        if p==self.stack_min[-1]:
            self.stack_min.pop()
        if p==self.stack_max[-1]:
            self.stack_max.pop()
        return p
    def top(self):
        if not self.stack:
            print("Stack is empty")
            return 
        t=self.stack[-1]
        return t
    def bottom(self):
        if not self.stack:
            print("Stack is empty")
        return self.stack[0]
    def getmin(self):
        if not self.stack_min:
            print("Min not found")
        return self.stack_min[-1]
    def getmax(self):
        if not self.stack_max:
            print("Max not found")
        return self.stack_max[-1]
    def printit(self):
        for i in range(len(self.stack)):
            if i==0:
                print(self.stack[i],end="")
            print(" -",self.stack[i],end="")
stack = mystack()
stack.push(3)
stack.push(5)
stack.push(6)
stack.push(1)
# stack.push(0)
stack.printit()
m=stack.getmin()
print(m)
t=stack.top()
print(t)
print(stack.bottom())



        
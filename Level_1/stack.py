class MinMaxStack:
    def __init__(self):
        self.stack = [] 
        self.min_stack = [] 
        self.max_stack = []  

    def push(self, x):

        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)


        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

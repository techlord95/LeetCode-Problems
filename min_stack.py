class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val:int) ->None:
        self.stack.append(val)
        #min val of itself and top of min stack , if stack is non empty 
        # lifo is the reason to check the topmost element
        val = min(val , self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) ->int:
        return self.stack[-1]
    
    def getMin(self) ->int:
        return self.minStack[-1]


# Time = O(1) and Space = O(n)
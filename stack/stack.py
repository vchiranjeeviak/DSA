class stack:
    stk = []  # Empty stack initialization
    top = -1  # Intializing top as -1

    def __init__(self, size):
        self.size = size  # Getting size of the stack while creating object

    def isFull(self):
        # return true if size is equal to current length
        return len(self.stk) == self.size

    def isEmpty(self):
        return len(self.stk) == 0  # return true if current length is 0

    def push(self, item):  # if stack is not full, push append an item
        if(self.isFull()):
            print("Stack is full")
            return
        self.stk.append(item)
        self.top += 1  # increment top after pushing
        self.peek()
        return

    def pop(self):  # if stack is not empty, return the top item and remove it
        if(self.isEmpty()):
            print("Stack is empty")
            return
        popped_item = self.stk.pop()
        self.top -= 1  # decrement top after popping
        self.peek()
        return popped_item

    def peek(self):  # return the top item if stack is not empty
        if(self.isEmpty()):
            print("Stack is empty")
            return
        print(self.stk[len(self.stk)-1])


stack_obj = stack(5)
stack_obj.pop()
stack_obj.push(1)
stack_obj.peek()
stack_obj.push(2)
stack_obj.push(3)
stack_obj.push(4)
stack_obj.push(5)
stack_obj.push(6)
stack_obj.pop()
stack_obj.pop()

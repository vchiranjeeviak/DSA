class Stack:

    def __init__(self, size):
        self.stack = []  # Empty stack initialization
        self.top = -1  # Intializing top as -1
        self.size = size  # Getting size of the stack while creating object

    def isFull(self):
        # return true if size is equal to current length
        return len(self.stack) == self.size

    def isEmpty(self):
        return len(self.stack) == 0  # return true if current length is 0

    def push(self, item):  # if stack is not full, push append an item
        if(self.isFull()):
            print("Stack is full")
            return
        self.stack.append(item)  # O(1)
        self.top += 1  # increment top after pushing
        self.peek()
        return

    def pop(self):  # if stack is not empty, return the top item and remove it
        if(self.isEmpty()):
            print("Stack is empty")
            return
        popped_item = self.stack.pop()  # O(1)
        self.top -= 1  # decrement top after popping
        self.peek()
        return popped_item

    def peek(self):  # return the top item if stack is not empty
        if(self.isEmpty()):
            print("Stack is empty")
            return
        print(self.stack[len(self.stack)-1])


stack_obj = Stack(5)
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

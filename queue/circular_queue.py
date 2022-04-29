class Circular_Queue:

    def __init__(self, size):  # Getting size and setting front and rear to -1
        self.cqueue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, num):
        if((self.rear + 1) % self.size == self.front):  # If queue is full
            print("Queue is full")
            return
        elif(self.front == -1):  # If queue is not full and not entered any item (initial phase)
            self.front = 0
            self.rear = 0
        else:  # If queue is not full but not in initial phase
            self.rear = (self.rear + 1) % self.size

        self.cqueue[self.rear] = num
        print(self.cqueue)
        return

    def dequeue(self):
        if(self.front == -1):  # If queue is empty
            print("Queue is empty")
            return
        elif(self.front == self.rear):  # If only one item is left, that is when front and rear are equal
            temp = self.cqueue[self.front]
            self.cqueue[self.front] = None
            self.front = -1
            self.rear = -1
            print(self.cqueue)
            return temp
        else:  # If not empty and not last item
            temp = self.cqueue[self.front]
            self.cqueue[self.front] = None
            self.front = (self.front + 1) % self.size
            print(self.cqueue)
            return temp

    def peek(self):
        if(self.front == -1):
            print("Queue is empty")
            return
        else:
            print(self.cqueue[self.front])
            return


cqueue_obj = Circular_Queue(5)
cqueue_obj.enqueue(1)
cqueue_obj.enqueue(1)
cqueue_obj.enqueue(1)
cqueue_obj.enqueue(1)
cqueue_obj.enqueue(4)
cqueue_obj.enqueue(1)
cqueue_obj.peek()
cqueue_obj.dequeue()
cqueue_obj.dequeue()
cqueue_obj.dequeue()
cqueue_obj.dequeue()
cqueue_obj.dequeue()
cqueue_obj.dequeue()

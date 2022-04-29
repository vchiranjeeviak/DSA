class Queue:

    def __init__(self, size):
        self.queue = [None] * size  # Initializing a queue
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, num):
        if(self.rear == self.size-1):  # Checking if the queue is full
            print("Queue is full or can't insert right now")
            return None
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.queue[self.rear] = num  # If not full, add item
        print(self.queue)
        return

    def dequeue(self):
        if(self.front == -1):  # Checking if queue is empty
            print("Queue is empty")
            return None
        elif(self.front == self.rear):
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            print(self.queue)
            return temp
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            print(self.queue)
            return temp

    def peek(self):
        if(self.front == -1):  # Checking if queue is empty
            print("Queue is empty")
            return None

        print(self.queue[self.front])  # If not return item at front


queue_obj = Queue(5)
queue_obj.enqueue(1)
queue_obj.enqueue(2)
queue_obj.enqueue(3)
queue_obj.enqueue(4)
queue_obj.enqueue(5)
queue_obj.enqueue(6)
queue_obj.dequeue()
queue_obj.dequeue()
queue_obj.dequeue()
queue_obj.peek()

queue_obj.dequeue()
queue_obj.peek()
queue_obj.dequeue()
queue_obj.dequeue()

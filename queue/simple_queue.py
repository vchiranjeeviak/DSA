class Queue:

    def __init__(self, size):
        self.queue = []  # Initializing a queue
        self.size = size

    def enqueue(self, num):
        if(len(self.queue) == self.size):  # Checking if the queue is full
            print("Queue is full or cant insert right now")
            return None

        self.queue.append(num)  # If not full, add item
        print(self.queue)

    def dequeue(self):
        if(len(self.queue) == 0):  # Checking if queue is empty
            print("Queue is empty")
            return None

        # returning item at front and removing it, if not empty
        print(self.queue[0])
        return self.queue.pop(0)

    def peek(self):
        if(len(self.queue) == 0):  # Checking if queue is empty
            print("Queue is empty")
            return None

        print(self.queue[0])  # If not return item at front


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
queue_obj.dequeue()
queue_obj.peek()
queue_obj.dequeue()
queue_obj.dequeue()

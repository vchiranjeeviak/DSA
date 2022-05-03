class Deque:
    def __init__(self, size):  # initializing a queue
        self.deque = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def isFull(self):  # return true if front is next to rear
        return ((self.rear+1) % len(self.deque)) == self.front

    def isEmpty(self):  # return true if both front and rear at -1
        return self.front == -1 and self.rear == -1

    def insert_front(self, num):
        if(self.isFull()):
            print("Deque is full")
            return
        elif(self.isEmpty()):  # If empty, assign 0 to both front and rear and insert at front
            self.front = 0
            self.rear = 0
            self.deque[self.front] = num
            print(self.deque)
            return
        elif(self.front == 0):  # If only 1 item is present (front=0), assign front to the last index
            self.front = self.size-1
            self.deque[self.front] = num
            print(self.deque)
            return
        else:  # Otherwise, decrement front and insert there
            self.front -= 1
            self.deque[self.front] = num
            print(self.deque)
            return

    def insert_rear(self, num):
        if(self.isFull()):
            print("Deque is full")
            return
        elif(self.isEmpty()):  # If empty, assign 0 to both front and rear and insert at front
            self.front = 0
            self.rear = 0
            self.deque[self.rear] = num
            print(self.deque)
            return
        else:  # Otherwise, increment rear and insert there
            self.rear += 1
            self.deque[self.rear] = num
            print(self.deque)
            return

    def delete_front(self):
        if(self.isEmpty()):
            print("Deque is empty")
            return
        # If only 1 item is present, delete and set 0 to front and rear
        elif(self.front == 0 and self.rear == 0):
            self.front = -1
            self.rear = -1
            temp = self.deque[0]
            self.deque[0] = None
            print(self.deque)
            return temp
        elif(self.front == self.size-1):  # IF front is at last index, delete and set front to 0
            temp = self.deque[self.front]
            self.deque[self.front] = None
            self.front = 0
            print(self.deque)
            return temp
        else:  # Otherwise, delete and increment front
            temp = self.deque[self.front]
            self.deque[self.front] = None
            self.front += 1
            print(self.deque)
            return temp

    def delete_rear(self):
        if(self.isEmpty()):
            print("Deque is empty")
            return
        # If only 1 item is present, delete and set 0 to front and rear
        elif(self.front == 0 and self.rear == 0):
            self.front = -1
            self.rear = -1
            temp = self.deque[0]
            self.deque[0] = None
            print(self.deque)
            return temp
        elif(self.rear == 0):  # IF rear is at 0, delete and set rear to last index
            temp = self.deque[self.rear]
            self.deque[self.rear] = None
            self.rear = self.size-1
            print(self.deque)
            return temp
        else:  # Otherwise, delete and decrement rear
            temp = self.deque[self.rear]
            self.deque[self.rear] = None
            self.rear -= 1
            print(self.deque)
            return temp


deque_obj = Deque(5)
deque_obj.insert_front(1)
deque_obj.insert_front(2)
deque_obj.insert_rear(5)
deque_obj.insert_rear(4)
deque_obj.insert_front(3)
deque_obj.insert_rear(6)
deque_obj.delete_rear()
deque_obj.delete_front()
deque_obj.delete_rear()
deque_obj.delete_front()
deque_obj.delete_rear()
deque_obj.delete_front()

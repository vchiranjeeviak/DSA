class Deque:
    def __init__(self, size):
        self.deque = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return ((self.rear+1) % len(self.deque)) == self.front

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def insert_front(self, num):
        if(self.isFull()):
            print("Deque is full")
            return
        elif(self.isEmpty()):
            self.front = 0
            self.rear = 0
            self.deque[self.front] = num
            print(self.deque)
            return
        elif(self.front == 0):
            self.front = self.size-1
            self.deque[self.front] = num
            print(self.deque)
            return
        else:
            self.front -= 1
            self.deque[self.front] = num
            print(self.deque)
            return

    def insert_rear(self, num):
        if(self.isFull()):
            print("Deque is full")
            return
        elif(self.isEmpty()):
            self.front = 0
            self.rear = 0
            self.deque[self.rear] = num
            print(self.deque)
            return
        else:
            self.rear += 1
            self.deque[self.rear] = num
            print(self.deque)
            return

    def delete_front(self):
        if(self.isEmpty()):
            print("Deque is empty")
            return
        elif(self.front == 0 and self.rear == 0):
            self.front = -1
            self.rear = -1
            temp = self.deque[0]
            self.deque[0] = None
            print(self.deque)
            return temp
        elif(self.front == self.size-1):
            temp = self.deque[self.front]
            self.deque[self.front] = None
            self.front = 0
            print(self.deque)
            return temp
        else:
            temp = self.deque[self.front]
            self.deque[self.front] = None
            self.front += 1
            print(self.deque)
            return temp

    def delete_rear(self):
        if(self.isEmpty()):
            print("Deque is empty")
            return
        elif(self.front == 0 and self.rear == 0):
            self.front = -1
            self.rear = -1
            temp = self.deque[0]
            self.deque[0] = None
            print(self.deque)
            return temp
        elif(self.rear == 0):
            temp = self.deque[self.rear]
            self.deque[self.rear] = None
            self.rear = self.size-1
            print(self.deque)
            return temp
        else:
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

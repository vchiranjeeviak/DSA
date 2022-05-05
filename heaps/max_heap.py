class Max_heap:

    def __init__(self):
        self.heap = []

    def insert(self, num):
        self.heap.append(num)
        len_of_heap = len(self.heap)
        if(len_of_heap > 1):
            for i in range(len_of_heap//2-1, -1, -1):
                self.heapify(i)

    def delete(self, index):
        len_of_heap = len(self.heap)
        self.heap[index], self.heap[len_of_heap -
                                    1] = self.heap[len_of_heap-1], self.heap[index]
        self.heap.pop()
        len_of_heap = len(self.heap)
        if(len_of_heap > 1):
            for i in range((len_of_heap//2)-1, -1, -1):
                self.heapify(i)

    def heapify(self, i):
        len_of_heap = len(self.heap)
        largest = i
        l = 2*i+1
        r = 2*i+2
        if(l < len_of_heap and self.heap[l] > self.heap[largest]):
            largest = l
        if(r < len_of_heap and self.heap[r] > self.heap[largest]):
            largest = r
        self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
        if(not (largest == i)):
            self.heapify(largest)

    def peek(self):
        if(len(self.heap) > 0):
            print(self.heap[0])
            return self.heap[0]
        else:
            print('Heap is empty')
            return

    def print_heap(self):
        print(self.heap)


heap_obj = Max_heap()
heap_obj.insert(1)
heap_obj.print_heap()
heap_obj.insert(2)
heap_obj.print_heap()
heap_obj.insert(3)
heap_obj.print_heap()
heap_obj.delete(2)
heap_obj.peek()
heap_obj.print_heap()
heap_obj.insert(4)
heap_obj.print_heap()
heap_obj.delete(0)
heap_obj.print_heap()

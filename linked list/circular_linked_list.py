from requests import delete


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# In circular linked list, we keep track of the tail of the list.
# IF we want to traverse, we can do that from tail.next


class Circular_Linked_List:
    def __init__(self):
        self.tail = None

    def insert_at_beginning(self, val):
        new_node = Node(val)
        if(not self.tail):
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    def insert_at_end(self, val):
        new_node = Node(val)
        if(not self.tail):
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, pos, val):
        new_node = Node(val)
        if(not self.tail):
            self.tail = new_node
        else:
            temp = self.tail.next
            count = 0
            while(temp and count < pos - 1):
                temp = temp.next
                count += 1
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, pos):
        temp = self.tail.next
        if(pos == 0):
            self.tail.next = temp.next
            temp = None
            return
        count = 0
        while(count < pos - 1):
            temp = temp.next
            count += 1
        deleting = temp.next
        temp.next = deleting.next
        deleting = None

    def print_list(self):
        temp = None
        if(self.tail.next):
            temp = self.tail.next
        else:
            temp = self.tail
        head_pointer = temp
        print(str(temp.val)+"->", end=" ")
        temp = temp.next
        while(not(temp == head_pointer)):
            print(str(temp.val)+"->", end=" ")
            temp = temp.next
        print()


cllist = Circular_Linked_List()
cllist.insert_at_beginning(1)
cllist.print_list()
cllist.insert_at_beginning(2)
cllist.print_list()
cllist.insert_at_end(3)
cllist.print_list()
cllist.insert_at_position(2, 4)
cllist.print_list()
cllist.delete(1)
cllist.print_list()
cllist.delete(0)
cllist.print_list()

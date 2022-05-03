class Node:
    def __init__(self, val):  # Each node has a val, pointer to point both next and prev
        self.val = val
        self.prev = None
        self.next = None

# Everything is similar to singly linked list except that we need to take care of prev pointer in every operation


class Doubly_Linked_List:  # Every list has a head
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        new_node = Node(val)
        if(not self.head):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, val):
        new_node = Node(val)
        if(not self.head):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, pos, val):
        new_node = Node(val)
        temp = self.head
        counter = 0
        while (temp and counter < pos-1):
            temp = temp.next
            counter += 1
        if(not temp):
            print("The position you specified is not available")
            return
        if(not temp.next):
            print("You are inserting at end, use insert_at_end function")
            return
        after_node = temp.next
        temp.next = new_node
        new_node.next = after_node
        new_node.prev = temp
        after_node.prev = new_node

    def delete(self, pos):
        counter = 0
        temp = self.head
        if(pos == 0):
            temp = temp.next
            self.head = temp
            temp.prev = None
            return
        while(temp and counter < pos - 1):
            temp = temp.next
            counter += 1
        if(not temp):
            print("The position you specified is not available")
            return
        if(not temp.next):
            print("Nothing to delete there")
            return
        deleting = temp.next
        temp.next = deleting.next
        if(deleting.next):
            deleting.next.prev = temp
        deleting = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(str(temp.val)+" <=>", end=" ")
            temp = temp.next


dllist = Doubly_Linked_List()
dllist.print_list()
print()
dllist.insert_at_beginning(1)
dllist.print_list()
print()
dllist.insert_at_beginning(2)
dllist.print_list()
print()
dllist.insert_at_end(3)
dllist.print_list()
print()
dllist.insert_at_position(2, 4)
dllist.print_list()
print()
dllist.delete(3)
dllist.print_list()
print()
dllist.insert_at_end(5)
dllist.print_list()
print()
dllist.delete(0)
dllist.print_list()
print()
dllist.delete(1)
dllist.print_list()
print()
dllist.delete(2)
dllist.print_list()

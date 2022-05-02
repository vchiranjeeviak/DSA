from logging.config import valid_ident


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Linked_List:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, new_val):
        new_node = Node(new_val)

        if(self.head is None):
            self.head = new_node

        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def insert_at_position(self, pos, new_val):
        new_node = Node(new_val)
        temp = self.head
        count = 0
        while(temp.next and count < pos-1):
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        temp = self.head
        self.head = self.head.next
        temp = None

    def delete_at_end(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        temp = self.head
        count = 0
        while(temp and temp.next and count < pos-1):
            temp = temp.next
            count += 1
        delete = temp.next
        temp.next = delete.next
        delete = None

    def search(self, item):
        temp = self.head
        count = 0
        while(temp):
            if(temp.val == item):
                print(item+" is in "+count+"th position")
                return count
            count += 1
            temp = temp.next
        print("Not found")
        return -1

    def sort_linked_list(self):
        current = self.head
        temp = Node(None)
        if current is None:
            return
        while(current):
            temp = current.next

            while(temp):

                if(current.val > temp.val):
                    current.val, temp.val = temp.val, current.val

                temp = temp.next

            current = current.next

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(str(temp.val)+",", end=" ")
            temp = temp.next


llist = Linked_List()
llist.insert_at_beginning(1)
llist.insert_at_beginning(2)
llist.print_linked_list()
print()
llist.insert_at_end(3)
llist.print_linked_list()
print()
llist.insert_at_position(2, 4)
llist.print_linked_list()
print()
llist.delete_at_position(2)
llist.print_linked_list()
print()
llist.delete_at_end()
llist.print_linked_list()
print()
llist.delete_at_beginning()
llist.print_linked_list()
print()
llist.insert_at_beginning(5)
llist.insert_at_beginning(6)
llist.insert_at_beginning(7)
llist.print_linked_list()
print()
llist.sort_linked_list()
llist.print_linked_list()
print()

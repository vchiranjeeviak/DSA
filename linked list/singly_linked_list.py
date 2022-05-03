class Node:

    def __init__(self, val):  # Every node has a value and pointer to next
        self.val = val
        self.next = None


class Linked_List:

    def __init__(self):  # Every list has a head initially having nothing
        self.head = None

    # new node points to head and head is changed to new node
    def insert_at_beginning(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    # traverse till the end, existing last node points to new node and new node points to null
    def insert_at_end(self, new_val):
        new_node = Node(new_val)

        if(self.head is None):
            self.head = new_node

        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next = new_node

    # traverse till before the pos, points points to after, before points to pos
    def insert_at_position(self, pos, new_val):
        new_node = Node(new_val)
        temp = self.head
        count = 0
        while(temp.next and count < pos-1):
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):  # shift head to head.next
        temp = self.head
        self.head = self.head.next
        temp = None

    def delete_at_end(self):  # Traverse till the end and point the last but one to none
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None

    # Traverse till the pos, before points to after and pos points to none
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

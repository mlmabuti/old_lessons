# create a node class
class Node:
    def __init__(self, data):
        self.data = data  # create data attribute to contain data
        self.next = None  # create pointer to point to next node


# create the linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # create head attribute for all linked lists

    def push(self, new_data):
        new_node = Node(new_data)  # create the new node
        new_node.next = self.head  # make new node point to old head
        self.head = new_node  # make the new node new head

    def insertAfter(self, position, new_data):  # take position and new data
        new_node = Node(new_data)  # create the new node
        if self.head is None:
            self.head = new_node
            return
        temp = self.head  # set temp as head to start from the beginning of the list
        k = 0
        while k < position:  # loop through until the position has been reached
            k += 1
            temp = temp.next  # this will allow you to move up the list
        new_node.next = temp.next
        temp.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        # if list is empty, set new_node as head
        if self.head is None:
            self.head = new_node
            return

        # else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # change the next of last node
        last.next = new_node

    # remove elements, ADD CHECKERS FOR EMPTY LIST OR SOME OTHER CASES
    def remove(self, position):
        temp = self.head
        j = 0

        while j < position - 1 and temp.next is not None:  # while previous of target position is not reached
            temp = temp.next  # and next node is not None
            j += 1  # move temp forward
        temp.next = temp.next.next  # once index position has been reached point the pointer
        # to the pointer of the next node, this will cut the target index position from the list
        # idk what happens to it or how to properly remove it from memory

    def traverse(self):
        temp = self.head
        while temp:  # move forward from the head until it is not None and print the data
            print(str(temp.data) + " ->", end=' ')
            temp = temp.next
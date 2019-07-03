# Insert a node in front of the linked list


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_front(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node


class Node:

    def __init__(self):
        self.data = None
        self.next = None

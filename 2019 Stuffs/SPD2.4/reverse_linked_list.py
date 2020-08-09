class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item


class LinkedList:
    
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items is not None:
            for v in items:
                self.append(Node(v))
    
    def __iter__(self):
        return LinkedListIterator(self.head)
    
    def append(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        
        new_node = node
        self.tail.next = new_node
        self.tail = new_node
        
        
example = LinkedList(range(10))


def reverse_linked_list(ll):
    prev = None
    curr = ll.head
    next_node = ll.head.next
    
    ll.tail = curr
    
    while next_node is not None:
        curr.next = prev
        prev = curr
        curr = next_node
        next_node = next_node.next
    curr.next = prev
    ll.head = curr
    

reverse_linked_list(example)

for v in example:
    print(v)

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
    
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        return LinkedListIterator(self.head)
    
    def append(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        
        new_node = node
        self.tail.next = new_node
        self.tail = new_node
        
        
example = LinkedList()
# 0 -> 1 -> 2 -> 3 -> 4 -> //  k = 2
# 2 -> 3 -> 4 -> 0 -> 1 -> //  k = 2

for i in range(5):
    example.append(Node(i))


def rotate(ll, k):
    if ll.head is None and ll.tail is None:
        return
    
    for _ in range(k):
        curr_node = ll.head
        ll.head = curr_node.next
        ll.tail.next = curr_node
        ll.tail = curr_node
        ll.tail.next = None
    

rotate(example, 2)

for v in example:
    print(v)

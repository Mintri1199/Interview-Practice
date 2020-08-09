# Given an array of k linked lists,
# each of whose items are in sorted order,
# combine all nodes (do not create new nodes) into a single linked list with all items in order.


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
        
        
linked_1 = LinkedList()  # 4-5-6-//
for i in range(4, 7):
    linked_1.append(Node(i))

linked_2 = LinkedList()
for i in range(3, 10):  # 3-4-5-6-7-8-9-//
    linked_2.append(Node(i))


example = [linked_1, linked_2]


def combine(ll_array) -> LinkedList:
    result = LinkedList()
    
    not_empty = True
    while not_empty:
        min_index = find_min(ll_array)
        if min_index is None:
            not_empty = False
        else:
            node = pop_left(ll_array[min_index])
            result.append(node)
    
    return result
    

def find_min(ll_array) -> int:
    curr_min = float('inf')
    min_index = None
    for index, ll in enumerate(ll_array):
        if ll.head is None:
            continue
        elif ll.head.data < curr_min:
            curr_min = ll.head.data
            min_index = index
    
    return min_index


def pop_left(ll):
    if ll.head is None and ll.tail is None:
        return
    head_node = ll.head
    ll.head = head_node.next
    return head_node


for v in combine(example):
    print(v)

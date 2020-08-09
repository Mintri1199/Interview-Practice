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


LL_1 = LinkedList()
LL_2 = LinkedList()
converge_node = Node(4)

for i in range(0, 3):
    LL_1.append(Node(i))
    
LL_1.append(converge_node)

for i in range(5, 10):
    LL_1.append(Node(i))

for v in ['a', 'b', 'c', 'd', 'e']:
    LL_2.append(Node(v))
    
LL_2.append(converge_node)
LL_2.tail = LL_1.tail


# return the convergence point
def find_convergence(list1, list2) -> Node:
    ll1_size = find_size(list1)
    ll2_size = find_size(list2)
    list_1_node = list1.head
    list_2_node = list2.head
    
    while list_1_node is not None or list_2_node is not None:
        if ll1_size > ll2_size:
            list_1_node = list_1_node.next
            ll1_size -= 1
        elif ll2_size > ll1_size:
            list_2_node = list_2_node.next
            ll2_size -= 1
        
        else:
            if list_1_node == list_2_node:
                return list_1_node
            
            list_1_node = list_1_node.next
            ll1_size -= 1
            
            list_2_node = list_2_node.next
            ll2_size -= 1
    
    return None


def find_size(linked_list) -> int:
    result = 0
    curr_node = linked_list.head
    while curr_node is not None:
        result += 1
        curr_node = curr_node.next
        
    return result

converge = find_convergence(LL_1, LL_2)

if converge is not None:
    print(converge.data)

# Remove all the occurrences of an element in a linked list

# Assumption:
# Positive int
# Non-empty
# input: target input
# might not presence in LL


# [0] -> [1] -> [3] -> //
# first solution:
# prev pointer
# while loop through the LL
# if data match the target
#


class Node(object):
    
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
    
    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

    
class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)
    
    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())
        
    def items(self):
        """Return a list of all items in this linked list.
Best and worst case running time: Theta(n) for n items in the list
because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    
    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None
    
    def length(self):
        """Return the length of this linked list by traversing its nodes.
Best and worst case running time:
Best: O(1) - where the length is like one
worst: O(n) - where we have to traverse each and every node """
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count
    
    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
raise ValueError if the given index is out of range of the list size.
Best case running time: O(1) under what conditions? [If the index is the head or tail]
Worst case running time: O(n) under what conditions? [If we have to loop through all the nodes]"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        
        current_node = self.head
        index_counter = 0
    

        # if index is head
        if index == 0:
            return self.head.data
        # if index is tail
        if index == self.size - 1:
            return self.tail.data
        
        while current_node is not None:  # O(n)
            # add to the index tracker and set the node to the next one.
            index_counter += 1
            current_node = current_node.next
            if index_counter == index:
                return current_node.data
    
    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
raise ValueError if the given index is out of range of the list size.
Best case running time: O(1) under what conditions? [If the list is empty or when there is 1 element in the list]
Worst case running time: O(n) under what conditions? [When we have to loop through the nodes to find the index]"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        new_node = Node(item)
        current_node = self.head
        previous_node = None
        index_counter = 0
    
        # if list is empty
        if self.size == 0:
            self.append(item)
            return self.size
        elif self.size == 1:
            if index == 0: self.prepend(item)
            return self.size
        
        while current_node is not None:
            index_counter += 1
            previous_node = current_node
            current_node = current_node.next
            if index_counter == index:
                # insert new node
                new_node.next = previous_node.next
                previous_node.next = new_node
                self.size += 1
                # make the new node the tail if it was inserted at the end
                if index == self.size - 1:
                    self.tail = new_node
                return self.size
    
    
    def append(self, item):
        """Insert the given item at the tail of this linked list.
Best and worst case running time: ??? under what conditions? [TODO]"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1
    
    
    def prepend(self, item):
        """Insert the given item at the head of this linked list.
    Best and worst case running time: ??? under what conditions? [TODO]"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node
        self.size += 1
        
    def remove_items(self, target):
        
        prev = None
        current = self.head
        
        while current is not None:
            # Check for head
            if current is self.head and current.data == target:
                self.head = current.next
                current.next = None
                current = self.head
                continue
            
            # check for tail
            if current is self.tail and current.data == target:
                if self.length() == 1:
                    self.tail = None
                else:
                    self.tail = prev
                    prev.next = None
                continue
                    
            # Found the data
            if current.data == target:
                prev.next = current.next
                current.next = None
                current = prev.next
            else:
                prev = current
                current = current.next
    
    
if __name__ == '__main__':
    linked_list = LinkedList([0, 1, 1, 1, 2, 3])
    linked_list.remove_items(2)
    assert linked_list.length() == 5
    print(linked_list)
    linked_list.remove_items(1)
    assert linked_list.length() == 2
    print(linked_list)
    linked_list.remove_items(0)
    assert linked_list.length() == 1
    assert linked_list.head.data == 3
    assert linked_list.tail.data == 3
    linked_list.remove_items(3)
    assert linked_list.length() == 0
    
    assert linked_list.head is None
    assert linked_list.tail is None
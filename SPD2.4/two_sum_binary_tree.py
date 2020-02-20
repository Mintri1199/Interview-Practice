from binary_tree import BinarySearchTree
import queue
# Two sum but binary search tree for the data structure

tree = BinarySearchTree([6, 4, 9, 1, 3, 7, 8])


def two_sum(input, t):
    result = []
    visited_nodes = set()
    # level order traversal and search for compliment
    q = queue.LifoQueue()
    q.put(input.root)
    
    while q.qsize() != 0:
        node = q.get()
        comp = t - node.data
        if comp in visited_nodes:
            result.append((node.data, comp))
        
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)
        
        visited_nodes.add(node.data)
        
    return None if len(result) == 0 else result


print(two_sum(tree, 10))

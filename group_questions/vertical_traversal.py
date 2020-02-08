# Definition for a binary tree node.
import binary_tree
from _collections import deque
# Assumption: all of the data are unique int

class Solution:
    
    def vertical_traversal(self, root: binary_tree.BinaryTreeNode):
        initial_array = []
        
        self._pre_order(0, 0, root, initial_array.append)  # O(n)
        
        sorted_array = sorted(initial_array, key=lambda el: [el[0], -el[1], el[2]])  # what is lambda is saying: sort it in asc ord for the x cordinate and reverse for the y coordinate  # O(nlogn)
        
        final_array = [[sorted_array[0][2]]]
        for i in range(1, len(sorted_array)):  # O(n)
            if sorted_array[i][0] == sorted_array[i - 1][0]:  # The node are at the same vertical
                final_array[-1].append(sorted_array[i][2])
            else:
                final_array.append([sorted_array[i][2]])
        return final_array
    
    def _pre_order(self, x, y, node, visit):
        """
        :param x: x coordinate of the node
        :param y: y coordinate of the node
        :param node: The current node when traversing
        :param visit: the function applying to the node
        :return: None if leaf
        """
        visit((x, y, node.data))
    
        if node.is_leaf():
            return
    
        self._pre_order(x - 1, y - 1, node.left, visit)
        self._pre_order(x + 1, y - 1, node.right, visit)
        
        
tree = binary_tree.BinarySearchTree([4, 2, 6, 1, 3, 5, 7])
# solution = Solution()

# print(solution.vertical_traversal(tree.root))

# solution with level order traversal and buckets
# 1 get the min and max range for the x coordinate of the tree
# 2 create an array of buckets
# 3 Do level order traversal


def better_vertical_traversal(root: binary_tree.BinaryTreeNode):
    max_range = 0
    min_range = 0
    
    def visit(x):
        nonlocal max_range
        nonlocal min_range
        if x > max_range:
            max_range = x
            
        if x < min_range:
            min_range = x
            
    # dfs to find the min and max range of the tree
    dfs_pre_order(0, root, visit)  # O(n)
    buckets = dict()
    
    for i in range(min_range, max_range + 1):  # O(range(min, max))
        buckets[i] = []
        
    # breadth first search to
    level_order(root, buckets)  # O(n)
    return [x for x in buckets.values()]  # O(range(min, max))


def dfs_pre_order(x, node, visit):
    node.data = (x, node.data)
    visit(x)
    if node.is_leaf():
        return
    
    dfs_pre_order(x - 1, node.left, visit)
    dfs_pre_order(x + 1, node.right, visit)


def level_order(start_node, buckets):

    def sort_bucket(value):
        buckets[value[0]].append(value[1])
    
    # Create queue to store nodes not yet traversed in level-order
    node_queue = deque()
    
    # Enqueue given starting node
    node_queue.append(start_node)
    # Loop until queue is empty
    while not len(node_queue) == 0:
        # Dequeue node at front of queue
        node = node_queue.popleft()
        # Visit this node's data with given function
        sort_bucket(node.data)
        # Enqueue this node's left child, if it exists
        if node.left:
            node_queue.append(node.left)
        # Enqueue this node's right child, if it exists
        if node.right:
            node_queue.append(node.right)
            

print(better_vertical_traversal(tree.root))

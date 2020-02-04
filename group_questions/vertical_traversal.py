# Definition for a binary tree node.
import binary_tree

# Assumption: all of the data are unique int

class Solution:
    #
    def verticalTraversal(self, root: binary_tree.BinaryTreeNode):
        initial_array = []
        
        self._pre_order(0, 0, root, initial_array.append)
        
        def _cmp(a, b):
            """Compare the two input to sorted them"""
            if a[]
            
        sorted_array = sorted(initial_array, key=_cmp)
        
        
        return initial_array
    
    def _pre_order(self, x, y, node, visit):
        """
        :param x: x coordinate of the node
        :param y: y coordinate of the node
        :param node: The current node when traversing
        :param visit: the function applying to the node
        :return: None if leaf
        """
        visit((x, y, node))
        
        if node.is_leaf():
            return
        
        self._pre_order(x - 1, y - 1, node.left, visit)
        self._pre_order(x + 1, y - 1, node.right, visit)
        
    
    
tree = binary_tree.BinarySearchTree([4, 2, 6, 1, 3, 5, 7])
solution = Solution()

print(solution.verticalTraversal(tree.root))

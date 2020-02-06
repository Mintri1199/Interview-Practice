# Definition for a binary tree node.
import binary_tree

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
solution = Solution()

print(solution.vertical_traversal(tree.root))

# solution with level order traversal and buckets
# 1 get the min and max range for the x coordinate of the tree
# 2 create an array of buckets
# 3 Do level order traversal

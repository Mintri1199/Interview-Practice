# Given a binary tree count the total amount of leaf nodes


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def number_of_leaves(self, root):
        # check if the initial iteration has doesn't have a root node
        if root is None:
            return 0

        if self.is_leaf(root):
            return 1

        leaves = 0

        leaves += self.number_of_leaves(root.left_child)

        leaves += self.number_of_leaves(root.right_child)

        return leaves

    def is_leaf(self, root):
        return root.left_child is None and root.right_child is None

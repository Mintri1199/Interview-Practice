# Given a binary tree (not a Binary Search Tree)
# Write a function that find out whether the binary tree is mirror or not
# assume that the node only have unique data


import binary_tree
# Small perfect tree
#      4
#    2   2
small_tree = binary_tree.BinaryTreeNode(4)
small_tree.right = binary_tree.BinaryTreeNode(2)
small_tree.left = binary_tree.BinaryTreeNode(2)

# Medium not mirror tree
medium_tree = binary_tree.BinaryTreeNode(4)
medium_tree.right = binary_tree.BinaryTreeNode(2)
medium_tree.left = binary_tree.BinaryTreeNode(2)

medium_left = medium_tree.left
medium_left.right = binary_tree.BinaryTreeNode(1)
medium_right = medium_tree.right
medium_right.right = binary_tree.BinaryTreeNode(1)


def is_mirror(root: binary_tree.BinaryTreeNode) -> bool:
    traverse_array = []
    
    dfs(root, traverse_array.append)
    
    print(traverse_array)
    
    left = 0
    right = len(traverse_array) - 1
    
    while left <= right:
        if traverse_array[left] != traverse_array[right]:
            return False
        left += 1
        right -= 1
        
    return True


def dfs(node, visit):
    
    if node.is_leaf():
        visit(node.data)
        return
        
    if node.left is not None:
        dfs(node.left, visit)
    else:
        visit(None)
    
    visit(node.data)
    
    if node.right is not None:
        dfs(node.right, visit)
    else:
        visit(None)


def better_is_mirror(root: binary_tree.BinaryTreeNode):
    if root.is_leaf():
        return True

    if root.left is None or root.right is None:
        return False
        
    left_tree_stack = [root.left]
    right_tree_stack = [root.right]
    
    while len(left_tree_stack) != 0 or len(right_tree_stack) != 0:
        left_node = left_tree_stack.pop()
        right_node = right_tree_stack.pop()
        
        if not compare_node(left_node, right_node):
            return False
        
        dfs_left_tree(left_node, left_tree_stack.append)
        dfs_right_tree(left_node, right_tree_stack.append)
        
    return True
            
        
def compare_node(left, right) -> bool:
    if left is None and right is not None:
        return False
    elif right is None and left is not None:
        return False
        
    return left.data == right.data
    
    
def dfs_right_tree(node, visit):
    # enqueue left child first
    visit(node.left)
    visit(node.right)


def dfs_left_tree(node, visit):
    # enqueue right child first
    visit(node.right)
    visit(node.left)

        
print(better_is_mirror(medium_tree))

char_dict = {
    '2': ['a', 'b', 'c'],
    '3': ['e', 'd', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

# Write a function that takes in a string of numbers

example_input = '22'


class Node:
    def __init__(self, string):
        self.string = string
        self.children = []


def combination_tree(input):
    node = Node('')
    result = list()
    _combination(input, 0, node, result.append)
    return result


def _combination(input, index, node, visit):
    if index == len(input):
        visit(node.string)
        return
        
    for char in char_dict[input[index]]:
        node.children.append(Node(node.string + char))
    
    for child in node.children:
        _combination(input, index + 1, child, visit)


print(combination_tree("234"))

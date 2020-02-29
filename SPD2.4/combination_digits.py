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

# base_case: when the ordinal values of the final string is the greatest example: "22" == 'cc'

example_input = '22'


# def validate(input, curr):
#     for i,v in enumerate(input):
#         if char_dict[v][-1] != curr[i]:
#             return False
#         return True
#
#
# def combination(input, curr_string=None):
#     if curr_string is not None and validate(input, curr_string):
#         return [curr_string]
#     string = ''
#     if curr_string is None:
#         for key in input:
#             string += find_char(key, None)
#         result = combination(input, string)
#         result.append(string)
#         return result
#
#     for i, key in enumerate(input):
#         string += find_char(key, curr_string[i])
#
#
#
#     result = combination(input, string)
#     result.append(string)
#     return result
#
#
# def find_char(key, curr):
#     if curr == char_dict[key][-1] or curr is None:  # Give it the first character if the current character is the last one or hasn't had one
#         return char_dict[key][0]
#     for c in char_dict[key]:
#         if ord(c) > ord(curr):
#             return c
#

# print(combination("23"))
# print(validate(example_input, 'aa'))  # Should be false
# print(validate(example_input, 'ab'))  # Should be false
# print(validate(example_input, 'cc'))  # Should be true


# print(find_char('2', 'a'))  # should be b
# print(find_char('2', 'b'))  # should be c
# print(find_char('2', 'c'))  # should be a
# print(find_char('9', 'y'))  # should be b

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

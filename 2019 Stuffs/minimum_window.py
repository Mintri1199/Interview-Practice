# Given a string S and a string T,
# find the minimum window in S which will contain all the characters in T in complexity O(n).
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"


def minimum_window_search(input, search) -> str:
    """
    :param input: The inputted string
    :param search: The target string for searching
    :return:
    """
    
    if len(input) < len(search):
        return ''
    
    left_pointer = 0
    min_range = []
    found = False
    current_size = len(input)
    window_map = {}
    target_dict = histogram(search)

    for i in range(len(input) + 1):
        if i != len(input):
            add_character(input[i], window_map)
        while check_contains(window_map, target_dict):
            found = True
            size = i - left_pointer
            if size < current_size:
                current_size = size
                min_range = [left_pointer, i + 1]
            window_map[input[left_pointer]] -= 1
            left_pointer += 1
            
    return input[min_range[0]:  min_range[1]] if found else ''
    
    
def check_contains(input_dict, target) -> bool:
    """
    Check whether the input_dict match the key and values of the target dict
    """
    for key in target:
        if key not in input_dict:
            return False
        elif input_dict[key] < target[key]:
            return False
    
    return True


def add_character(c, d):
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

    
def histogram(string) -> dict:
    result = {}
    for c in string:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result


print(minimum_window_search("a", "b"))

# I wasn't able to finish the interview so I am coding up what I had.
# Given a string, return the starting and end index of the longest substring
def longest_substring(text):
    longest_sub = []  # Where I track the indexes
    longest_counter = 0  # Keep track of the length of the longest substring
    curr_sub = []  # The indexes of the current substring that I am searching
    curr_count = 0  # The length of the current substring
    char_set = set()
    for index, char in text.enumerate(): # Wrong syntax
        for inner_index in range(index, len(text) -1):
            if text[inner_index] not in char_set:
                char_set.add(text[inner_index])
                curr_count += 1
                curr_sub.append(inner_index)
            
            else:
                if curr_count > longest_counter:
                    longest_counter = curr_count
                    longest_sub = [curr_sub[0], curr_sub[-1]]
                    curr_count = 0
                    curr_sub = []
                # Didn't even reset the set
                # char_set = set()
                break
    
    return longest_sub

example = "ababqerba"

print(longest_substring(example))

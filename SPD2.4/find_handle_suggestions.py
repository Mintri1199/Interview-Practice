# String Problems
# Twitter Follow Suggestions
# You’re working an internship at Twitter and are tasked to improve suggestions for accounts to follow, which already works great for established
# accounts because it uses content from your tweets and other accounts you follow to suggest new ones. However, when a new user signs up none of this
# information exists yet, but Twitter still wants to make some follow suggestions. Your team asked you to implement a function that accepts a new
# user’s handle and an array of many other users’ handles, which could be very long – Twitter has over 330 million active accounts! You need to
# calculate a similarity score between a pair of handles by looking at the letters each contains and scoring +1 for each letter that occurs in both
# handles and –1 for each letter that occurs in only one handle. Your function should return 2 handles from the array that have the highest
# similarity score to the new user’s handle.
#
# Example execution:
# suggest('iLoveDogs', ['DogeCoin', 'YangGang2020', 'GodIsLove', 'HodlForLife', 'fakeDonaldDrumpf', 'BernieOrBust'])
# should return   ['GodIsLove', 'DogeCoin']

from binaryheap import BinaryMinHeap


def get_suggestion(org_handle, handle_array) -> [str]:
    assert len(handle_array) >= 2
    
    suggestion_min_heap = BinaryMinHeap()
    
    handle_set = set(org_handle)
    
    for handle in handle_array:
        curr_score = get_score(handle_set, handle)
        
        if suggestion_min_heap.size() < 2:
            suggestion_min_heap.insert((handle, curr_score))
            
        elif curr_score > suggestion_min_heap.get_min()[1]:
            suggestion_min_heap.replace_min((handle, curr_score))
    
    return [x[0] for x in suggestion_min_heap.items]


def get_score(handle_set, handle_str) -> int:
    score = 0
    for c in handle_str:
        if c not in handle_set:
            score -= 1
        else:
            score += 1
    return score


handles = ['DogeCoin', 'YangGang2020', 'GodIsLove', 'HoldForLife', 'fakeDonaldDrumpf', 'BernieOrBust']
org_hand = "iLoveDogs"

print(get_suggestion(org_hand, handles))

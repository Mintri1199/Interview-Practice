
def find_indexes(input, target, curr=0, start=None, end=None):
    if input[curr] != target and start is not None:
        return curr - 1
    elif curr == len(input) - 1:
        if start is not None:
            return curr
        else:
            return
    
    
    
        
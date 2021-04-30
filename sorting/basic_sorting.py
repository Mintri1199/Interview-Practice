# Implement the following basic sorting algorithms
# bubble sort
# insertion sort
# selection sort

num_arr = [61, 83, 100, 92, 17, 84, 88]

def bubble_sort(arr):
    # Sort the input array using the bubble sort algorithm
    if len(arr) <= 1:
        return

    for num_sorted in range(1, len(arr)):
        is_sorted = True 
        for i in range(len(arr) - num_sorted):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        
        if is_sorted:
            break
    
def selection_sort(arr):
    # Sort the arry using the Selection Sort algorithm
    if len(arr) <= 1:
        return
    

    for offset in range(len(arr)):
        min_index = offset
        min_num = arr[offset]

        is_sorted = True

        for i in range(offset, len(arr)):
            if arr[i] <= min_num:
                min_index = i
                min_num = arr[i]
                is_sorted = False

        if is_sorted:
            break
        else:
            # Swap
            arr[offset], arr[min_index] = arr[min_index], arr[offset]

def _is_sorted(arr) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False

    return True


def insertion_sort(arr):
    # Sort the array using the Insertion Sort algorithm
    if len(arr) <= 1:
        return
    
    offset = 0
    is_sorted = False
    while not is_sorted:
        for i in range(offset, -1, -1):
            if arr[i] <= arr[i + 1]:
                break
            else:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        offset += 1
        is_sorted = _is_sorted(arr)


# bubble_sort(num_arr)
# selection_sort(num_arr)
# insertion_sort(num_arr)

print(num_arr)





    
# Given an array oif n numbers and a count k find the k largest values in the array a

import heapq

example = [5, 1, 3, 6, 8, 2, 4, 7]
count = 3
# Output = [6,8,7]


# 1 sort the array and pop the Kth number  O(nlogn + k)
def k_largest_sorted(nums, count) -> [int]:
    assert len(nums) >= count
    nums = sorted(nums)
    return [nums.pop() for _ in range(count)]
    

# 2 don't sort but compare each numbers with k size array  O(n * 2k)
def k_largest_not_sorted(nums, count) -> [int]:
    assert len(nums) >= count
    result = [float('-inf')] * count
    curr_min = float('-inf')
    for num in nums:   # O(n)
        if num > curr_min:
            for i, value in enumerate(result):  # 0(k)
                if value == curr_min:
                    result[i] = num
                    curr_min = min(result)  # O(k)
                    break
        
    return result


# 3 use a min heap to keep track of the largest minimum
def k_largest_heap(nums, count) -> [int]:
    assert len(nums) >= count
    result = [float('-inf')] * count
    
    for num in nums:
        if num > result[0]:
            heapq.heapreplace(result, num)
        
    return result

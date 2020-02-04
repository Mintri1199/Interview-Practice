# The classic twosum with multiple solutions
# 1 Double for loops O(n^2)
example = [3,5,1,5,8,0,4,2, 7, 11, 15]
target = 16


def twosum_2loops(nums, target) -> [int]:
    
    for i, num in enumerate(nums):
        diff = target - num
        if i == len(nums) - 1:
            return None
        for j in range(i + 1, len(nums)):
            if nums[j] == diff:
                return [num, nums[j]]


# 2 sort it and use binary search O(nlogn) + O(logn)
def twosum_binary(array, target):
    sorted_array = sorted(array)
    
    for i, num in enumerate(sorted_array):
        if i == len(array) - 1:
            return None
        
        diff = target - num
        found = binary_search(sorted_array, i, diff)
        if found:
            return [num, diff]
    

def binary_search(array, offset, target) -> bool:
    left = 0 + offset
    right = len(array) - 1
    
    while left <= right:
        middle = (right + left) // 2
        if array[middle] == target:
            return True
        elif array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
            
    return False


# 3 Build a dictionary as you pass through the array once

def twosum_dict(nums, target):
    nums_set = set()
    
    for num in nums:
        if num not in nums_set:
            nums_set.add(num)
            
        diff = target - num
        if diff in nums_set:
            return [num, diff]
            
    return None


# 4 two pointers but not binary search essentially O(n^2) but have a better start
def twosum_pointers(nums, target):
    nums = sorted(nums)
    med_i = len(nums) // 2
    med_value = nums[med_i]
    pointer = len(nums) - 1 if (target - med_value) > med_value else 1
    
    if pointer == 1:
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return None
            diff = target - nums[i]
            for j in range(pointer + i, len(nums)):
                if nums[j] == diff:
                    return [nums[i], diff]
    else:
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return None
            diff = target - nums[i]
            for j in range(pointer, i + 1, -1):
                if nums[j] == diff:
                    return [nums[i], diff]


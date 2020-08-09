# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is close to t

arr_1 = [9, 13, 8, 1, 2, 4, 7]
arr_2 = [3, 17, 4, 14, 6]
target = 20


# 1 create a set of the bigger array then loop through the small one while reducing the thresh hold
def closest_sum(nums1, nums2, target):
    smaller, bigger = (nums1, nums2) if min([len(nums1), len(nums2)]) == len(nums1) else (nums2, nums1)
    bigger_set = set(bigger)
    lowest_thresh = float('inf')
    result = []
    
    for num in smaller:
        curr_thresh = 0
        diff = target - num
        
        while curr_thresh <= lowest_thresh:
            if diff + curr_thresh in bigger_set:
                if curr_thresh <= lowest_thresh:
                    result.append([num, diff + curr_thresh])
                    lowest_thresh = curr_thresh
                    
            if diff - curr_thresh in bigger_set:
                if curr_thresh <= lowest_thresh:
                    result.append([num, diff - curr_thresh])
                    lowest_thresh = curr_thresh
    
            curr_thresh += 1
        
    return result

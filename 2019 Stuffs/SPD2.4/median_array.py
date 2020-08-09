# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0

# Example 2:
#
nums1 = [1, 2]
nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

# if able to use median function
#
# from numpy import median
#
# def built_in_median(nums1, nums2):
#     new_arr = nums1 + nums2
#     return median(new_arr)
#
#
# print(built_in_median(nums1, nums2))


def median_two_arrays(arr1, arr2):
    i_1 = 0
    i_2 = 0
    size = (len(arr1) + len(arr2)) // 2
    curr_item = 0
    prev = curr_item
    for _ in range(size):
        if arr1[i_1] <= arr2[i_2]:
            prev = arr1[i_1]
            curr_item = arr2[i_2]
        else:
            prev = arr2[i_2]
            curr_item = arr1[i_1]

        i_1 += 1
        i_2 += 1
        
    return curr_item if size % 2 != 0 else (curr_item + prev) / 2

# find the right partition of both arrays that max of right partition of the shorter array is less than the


def median(num1, num2):
    smaller = []
    bigger = []

    if len(num1) <= len(num2):
        smaller = num1
        bigger = num2
    else:
        smaller = num2
        bigger = num1



    result = None
    
    return median

def partition(arr, start, end):
    return

print(median_two_arrays(nums1, nums2))


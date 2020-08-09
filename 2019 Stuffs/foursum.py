# https://leetcode.com/problems/4sum/
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such
# that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# Things to notes:
#     * The array is not sorted
#     * Assuming the array can be empty
#     * Assuming invalid target returns an empty array

# Hmm.. Its look like I need to find all the permutations in the array, then get rid of the duplicate combination.
# An easy way to do this will be using the built in tools that python offered itertools

from itertools import permutations


# NAIVE solution
def four_sum_itertools(nums, target):
    if len(nums) < 4:  # O(1)
        return []
    elif len(nums) == 4 and sum(nums) == target:  # O(1)
        return [nums]

    # Get all the permutation that contains 4 elements
    # O(n!) where n is the length of the inputted array
    poss_perm = permutations(nums, 4)

    answer_array = []  # [()]
    duplicate = False
    for perm in poss_perm:
        if sum(perm) == target:  # Check if the sum of the current permutation is equal to the target

            for answer in answer_array:  # Check if all the elements in the current perm match one of the answer arrays
                if set(perm) == set(answer):  # O(2p) where p is 4
                    duplicate = True
                    break

            if duplicate is False:
                answer_array.append(perm)

            duplicate = False
    return answer_array

# One of the problems of this solution is that we can't control or modify the permutation code.
# Thus if we can move the sum and duplicate checks while making the permutations, we can avoid removing the duplicate
# after the permutations are created. This will exceed the time limit in leetcode.


# So in our next solution, we will implement our own custom permutation algorithm but include the two require checks in
# in process
nums = [1, 0, -1, 0, -2, 2]

print(four_sum_itertools(nums, 0))
#
# def four_sum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[List[int]]
#     """

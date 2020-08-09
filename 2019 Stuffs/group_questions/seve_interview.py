# Given a length and height that represent a 2D matrix
# ie: 2,2
#   0,0,  0,1,  0,2
#   1,0,  1,1,  1,2
#   2,0,  2,1,  2,2
# You start from 0,0 and can only move down and right
# Write a function that count all possible path to the most bottom right corner


# def paths(l, h):
#     if l < 0 or h < 0:
#         return 0
#
#     if l == 0 and h == 0:
#         return 1
#
#     result = 0
#
#     result += paths(l - 1, h)
#     result += paths(l, h - 1)
#
#     return result
#
#
# print(paths(2, 2))



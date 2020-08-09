# A boomerang is a set of 3 points that are all distinct and not in a straight line.
#
# Given a list of three points in the plane, return whether these points are a boomerang.

# Input: [[1,1],[2,3],[3,2]]
# Output: true

# Input: [[1,1],[2,2],[3,3]]
# Output: false
import operator
import functools

def isBoomerang(points):
    y = set([x[1] for x in points])
    x = set([x[0] for x in points])
    bool_list = map(lambda x: x[0] == x[1], points)

    if functools.reduce(operator.and_, bool_list, True):
        return False

    elif len(y) == 1 or len(x) == 1:
        return False

    elif len(set([(x[0], x[1]) for x in points])) != 3:
        return False

    return True


def betterBoomerang(points):
    # Use math
    A = points[0]
    B = points[1]
    C = points[2]
    return A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]) != 0



print(betterBoomerang([[1, 1], [2, 3], [3, 2]]))  # True
#
print(betterBoomerang([[1, 1], [2, 2], [3, 3]]))  # False

print(betterBoomerang([[0, 1], [1, 1], [2, 1]]))  # False

print(betterBoomerang([[0, 0], [2, 2], [1, 0]]))  # True



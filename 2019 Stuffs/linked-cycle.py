# https://leetcode.com/problems/linked-list-cycle/
# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Ok, so one way to solve this is to some how track all the nodes we have seen.
# Then if we saw a node again, that mean that there's a cycle in the linked list.

# So let's assume that the nodes can have duplicate values, this means that we could use a set to store our nodes.


def has_cycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    seen_nodes = set()  # A dictionary of the node that we saw when traversing the linked list

    while head is not None:  # loop until the head is None, which mean the previous head was a tail  O(n)
        if head in seen_nodes:  # O(1)
            return True

        else:
            seen_nodes.add(head)

        head = head.next

    return False

# How to do this with O(1) constant space time complexity

# Hmm, Okay this might need another approach. This time we can not use a set to keep track the nodes that we saw ....
# maybe we can solve using similar approach from the palindrome problem. In the palindrome problem, we used a left and
# a right pointers, then if they cross each other, it means that it is a palindrome. How about we use two pointers for
# this problem?

# So I am imagining a track field, but I was usually one of the slow runners, but there are some people that are faster
# than me. Thus when doing laps, they would eventually lap me. So using that experience, how about we recreate that
# situation but in code to solve this problem!

# So we will need two pointers, a slow pointer and a fast pointer. The different of the fast pointer is that it is one
# node ahead of the slow pointer, thus if there's a cycle the fast pointer could be in the same position as the slow
# pointer.


def has_cycle_no_space(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow_pointer = head
    fast_pointer = head  # One node ahead of the slow pointer
    while fast_pointer is not None and fast_pointer.next is not None:  # loop until the fast pointer reach the tail
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
                return True

    return False

# Given an list of integers, write a method - max_gain - that returns the maximum gain. Maximum Gain is defined as
# the maximum difference between 2 elements in a list such that the larger element appears after the smaller element.
# If no gain is possible, return 0.

# max_gain([100,40,20,10]) ==> 0
# max_gain([0,50,10,100,30]) ==> 100


def max_gain(input_list):
    gain = 0
    previous = input_list[0]

    for num in input_list:
        if num > previous:
            if num > gain:
                gain = num
            previous = num

    return gain

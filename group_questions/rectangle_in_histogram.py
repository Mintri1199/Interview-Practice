# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

# Input: [2,1,5,6,2,3]
# Output: 10
# Explanation: width: 2 [5,6], height: 5 [5,6]

example = [2, 1, 5, 6, 2, 3]

bigger_example = [2, 4, 6, 1, 4, 4, 4, 6]


def largest_rectangle(histogram):  # O(n*K*n-1)
    max_area = 0
    
    for i, num in enumerate(histogram):
        for val in range(1, num + 1):
            height = val
            width = 1
            for j in range(i + 1, len(histogram)):
                next_val = histogram[j]
                
                if next_val >= height:
                    width += 1
                else:
                    if (next_val * (width + 1)) >= (height * width):
                        height = next_val
                    else:
                        break
            if (height * width) >= max_area:
                max_area = height * width
        
    return max_area
    
    
def better_largest_rectangle(histogram):  # Using stack
    histogram.append(0)  # A stop value
    indices_stack = [-1]  # -1 direct to the stop value
    answer = 0
    
    for i in range(len(histogram)):  # 0(n)
        while histogram[i] < histogram[indices_stack[-1]]:
            height = histogram[indices_stack.pop()]
            width = i - indices_stack[-1] - 1
            answer = max(answer, (height * width))
        indices_stack.append(i)
        
    histogram.pop()  # Remove the stop value
    return answer


print(better_largest_rectangle(bigger_example))

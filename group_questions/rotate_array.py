# Rotate 2D matrix

# Write a function that rotate the value in a 2D matrix 90 degree
# 1 2 3         7 4 1
# 4 5 6   ->    8 5 2
# 7 8 9         9 6 3

example = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

bigger_example = [[1, 2, 3, 5, 6],
                  [7, 8, 9, 10, 11],
                  [12, 13, 14, 15, 16],
                  [17, 18, 19, 20, 21],
                  [22, 23, 24, 25, 26]]


def rotate_array(matrix):
    
    offset = 0
    
    for i in range(len(matrix) // 2):
        if len(range(offset, len(matrix) - offset - 1)) == 1:
            continue
            
        for j in range(offset, len(matrix) - offset - 1):
            first_val = matrix[offset][j]
            sec_val = matrix[j][-1 - offset]
            third_val = matrix[len(matrix) - 1 - offset][len(matrix) - 1 - j]
            fourth_val = matrix[len(matrix) - 1 - j][offset]
            matrix[offset][j], matrix[j][-1 - offset], matrix[len(matrix) - 1 - offset][len(matrix) - 1 - j], matrix[len(matrix) - 1 - j][offset] = fourth_val, first_val, sec_val, third_val
        
        offset += 1
            
    return matrix


result = rotate_array(bigger_example)

for v in result:
    print('\t'.join([str(x) for x in v]))

# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


def count_one_digit(n):
    if n <= 0:
        return 0
    
    current_n, x, answer = n, 1, 0
    while current_n > 0:
        digit = current_n % 10
        current_n /= 10
        answer += current_n * x
        if digit == 1:
            answer += n % x + 1
        elif digit > 1:
            answer += x
        x *= 10
    return answer

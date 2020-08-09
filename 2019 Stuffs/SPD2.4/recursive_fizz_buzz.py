# Do fizz buzz but recursively


def fizz_buzz(start, end):
    assert start <= end
    if end == start:
        return [logic(end)]
    result = fizz_buzz(start, end - 1)
    result.append(logic(end))
    return result
    
    
def logic(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num
    

print(fizz_buzz(1, 20))

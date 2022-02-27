#!/bin/python3 

# split() with a specified separator doesn't group consecutive whitespaces (please kindly refer to split() doc)
# a test case is 'hello    world  lol' that should be converted to 
# 'Hello    World  Lol' and not 'Hello World Lol'

# Complete the solve function below.
def solve(s):
    return ' '.join([term.capitalize() for term in s.split(' ')])

    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

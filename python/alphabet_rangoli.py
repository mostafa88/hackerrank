# alphabet-rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
from string import ascii_lowercase
import string


def print_rangoli(n):
   # your code goes here
    # row len = ( 2 * number_of_characters -1 ) + ( number of dashes that no dashes is (2 * number_of_characters -1) -1 ) 
    row_len = (2*n - 1)  + (2*n -1) -1 
    stack = []

    for i in range(n-1,-1,-1):
        build_str = ''
        if n-i == 1:
            build_str = ascii_lowercase[i:n]
        else:
            build_str = ascii_lowercase[i:n][::-1] +  ascii_lowercase[i+1:n]
            
        build_str = '-'.join(list(build_str))
        dash_size = (row_len - len(build_str)) // 2
        row  = dash_size * '-' + build_str + dash_size * '-'
        
        if i > 0: # do not append middle line to stack
            stack.append(row)
        print(row)

    while len(stack) > 0 :
        row = stack.pop()
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
   
   
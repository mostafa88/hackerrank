# title: Sum and Prod
# link: https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# Solution: 
# note: a sample code to read a matrix form input to a numpy matrix

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    entries = []
    for i in range(n):
        entries.append(list(map(int, input().split())) )
    matrix = np.array(entries).reshape(n, m) # to build a matrix from a flat 2D list
    print(np.prod(np.sum(matrix, axis=0)))

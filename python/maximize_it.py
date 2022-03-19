# title: Maximize it!
# link: https://www.hackerrank.com/challenges/maximize-it/problem
# Solution: using product function to build a tuple with select 1 item from each list, then calulate sum of i**2 in the list 
#       and then mod to M. at last find the maximum between maxes.
# note:


from itertools import product
import math
k , m = map(int, input().split())
lists = []
for i in range(k):
    lists.append( map(int,input().split()[1:]) )

maxs =  list(map( lambda x: sum(i**2 for i in x)%m ,product(*lists)))
print(max(maxs))


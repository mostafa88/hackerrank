# title: company_logo
# link: https://www.hackerrank.com/challenges/most-commons/problem
# Solution: read data using Counter to count each element, then read the dictionary to a list of touple
#   to be sortable using lambda function , cause the lambda function get only 1 argument and it can be sort using a tuple.
# note:

from collections import Counter

if __name__ == '__main__':
    s = input()
    counter = Counter(s)
    list = [(k, v) for k, v in counter.items()]
    list = sorted(list,key=lambda x: (-x[1],x[0])) # sort by first element descending, then second element ascending.
    for i in range(3):
        print(list[i][0], list[i][1])
    
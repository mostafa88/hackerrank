# title: collections-counter
# link: https://www.hackerrank.com/challenges/collections-counter/problem?
# Solution:
# note:

from collections import Counter

if __name__ == '__main__':
    n_shoes = int(input())
    shoes=dict()
    shoes = Counter(map(int, input().split()))
    n_customer = int(input())

    total_money = 0
    for c in range(n_customer):
        shoe_size, price = map(int,input().split())
        if shoes[shoe_size] > 0:
            total_money += price
            shoes[shoe_size] -= 1
    print(total_money)

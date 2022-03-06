# title: Collections namedtuple
# link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Solution: 
# note: using namedtuple help to create a dynamec structure with arbitary fields and field order
from collections import namedtuple
n = int(input())
headers = input()
Student = namedtuple('Student',headers)
avg = 0
for i in range(n):
    h1,h2,h3,h4 = input().split()
    s = Student(h1,h2,h3,h4)
    avg += int(s.MARKS)
print("{:.2f}".format(avg/n))
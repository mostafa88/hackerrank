# title: Find Angle MBC
# link: https://www.hackerrank.com/challenges/find-angle/problem
# Solution: to solve this problem use 2 Geometric theorem:
# 1: finding the median in in triangle: ma= sqrt((2b**2 + 2c**2 - a**2)/4)
# https://fa.wikipedia.org/wiki/%D9%85%DB%8C%D8%A7%D9%86%D9%87_%D9%85%D8%AB%D9%84%D8%AB 
# and as it's a trianble with 90 degree, so the median of 90 degree is half of the chord
# 2: the Cosine Theorem: a**2 = b**2 + c**2 - 2bc*cos(A)
# note:

import math
ab = float(input())
bc = float(input())
# ab , bc = 10,20
mb = (math.sqrt(ab*ab + bc*bc))/2

theta = math.acos(bc/(mb*2))
theta_deg = math.degrees(theta)
print(f"{round(theta_deg)}{chr(176)}")

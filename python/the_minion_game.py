#!/bin/python3 

# the-minion-game
# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

# note: as the input order is 10^6 the O(n) Solution required
# for "abcd" example there is the following substirng
# a,ab,abc,abcd
# b,bc,bcd
# c,cd
# d
# as you see, number of substring that started wiht i'th index is len(string) - i OR n-i
# so just need to check the string[i] is as vowels or not, then sum up it's substirng to corospoind value stuart of kevin


def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    string_size = len(string)
    for i in range(string_size):
        if string[i] in ('AEIOU'):
            kevin += string_size - i
        else:
            stuart += string_size - i
    
    if kevin > stuart:
        print("Kevin", kevin )
    elif stuart > kevin:
         print("Stuart", stuart )
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
# title: merge-the-tools
# link: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Solution: separate string to k equal length substring , the iterate each of them.
# for each c in substr check it's existence in a set, if not exist add it to result string and set too.
# note: checking and adding an element to a set is O(1), as we must iterate all the string, so the solution is O(n)

def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        t = string[i:i + k]
        check = set()
        res = ""
        for c in t:
            if c not in check:
                check.add(c)
                res += c
        print(res)


if __name__ == "__main__":
    s, k = input(), int(input())
    # s, k = "AABCAAADA", 3
    merge_the_tools(s, k)

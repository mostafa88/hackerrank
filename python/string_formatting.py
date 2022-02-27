# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    s = "{0:b}".format(number) # binary
    padding = len(s)

    # your code goes here
    for i in range(1,number+1):
        print("{0:d}".format(i).rjust(padding),"{0:o}".format(i).rjust(padding),
              "{0:X}".format(i).rjust(padding),"{0:b}".format(i).rjust(padding))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

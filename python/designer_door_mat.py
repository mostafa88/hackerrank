# Enter your code here. Read input from STDIN. Print output to STDOUT
from os import sep


def print_line(row_index,width,height):
   
    if row_index == (width//2) + 1:
        print((height-7)//2 * '-' ,"WELCOME",(height-7)//2 * '-',sep='')
        return
    elif row_index <  (width//2) + 1:
        line_count = row_index * 2 - 1
    else :
        line_count = (width - row_index) * 2 + 1
    
    dot_count = line_count*2
    dash_count = height - (line_count + dot_count)
    print(dash_count//2 * '-',line_count * '.|.',dash_count//2 * '-',sep='')
        
if __name__ == "__main__":
    width,height = map(int,input().split(sep=' '))
    for i in range(1,width+1) :
       print_line(i,width,height)

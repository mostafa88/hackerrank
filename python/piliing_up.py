# title: Pilling up!
# link: https://www.hackerrank.com/challenges/piling-up/problem
# Solution: find maximum(leftmost,rightmost) wich is less than last_selected item.other wise it's not possible.
# note:

test_case = int(input())
for _ in range(test_case):
    cube_size = int(input())
    cube = list(map(int,input().split()))
    start = 0
    end = cube_size -1
    last_selected = 2**31
    iterated = 0
    while(iterated < cube_size ):
        if last_selected >= min(cube[start],cube[end]):
            if cube[start] >= cube[end]:
                if cube[start] <= last_selected:
                    last_selected = cube[start]
                    start += 1
                else: # 
                    last_selected = cube[end]
                    end -=1
            else: # cube[start] < cube[end]:
                if cube[end] <= last_selected:
                    last_selected = cube[end]
                    end -=1
                else:
                    last_selected = cube[start]
                    start += 1
        else:
            print('No')
            break
        iterated += 1
        
    if(iterated == cube_size):
        print('Yes')
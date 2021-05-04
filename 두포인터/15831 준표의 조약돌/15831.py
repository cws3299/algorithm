import sys
sys.stdin = open('15831.txt','r')
from copy import deepcopy

n,b_max,w_max = map(int, input().split())
paths = list(input())

ll = len(paths)

left = 0
answer = 0

# end = ll
flag = False
while left < ll:
    right = deepcopy(left)
    black = 0
    white = 0
    if paths[left] == 'B':
        black += 1
    else:
        white += 1

    # if black > b_max:
    #     flag = True
    #     left += 1
    #     continue

    # print(left,paths[left:ll].count('W'))
    if black > b_max or paths[left:ll].count('W') < w_max:
        left += 1
        continue

    right += 1

    if flag == False:
        if answer < right-left:
            if black <= b_max and white >= w_max:
                flag = True
                answer = 0

    while right < ll:
        if paths[right] == 'B':
            black += 1
        else:
            white += 1

        if black <= b_max and white >= w_max:
            if answer < right-left:
                flag = True
                answer = right - left
        elif black > b_max:
            break

        right += 1

    left += 1
    # end = ll


    
if flag == True:
    print(answer+1)
else:
    print(0)
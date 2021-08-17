import sys
sys.stdin = open('15685.txt','r')
from collections import deque
from copy import deepcopy

n = int(input())
arr = [[0]*101 for _ in range(101)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]

for _ in range(n):
    ar = list(map(int, input().split()))

    y = ar[1]
    x = ar[0]
    d = ar[2]
    g = ar[3]

    stack = deque()
    arr[y][x] += 1
    stack.append(d)
    check = -1

    while True:

        if check == g:
            break

        tmp = deepcopy(stack)
        stack2 = deque()

        while stack:
            d = stack.pop()

            if d == 0:
                ny = y+dy[0]
                nx = x+dx[0]
                arr[ny][nx] += 1
                x += 1
                stack2.append(1)
            elif d == 1:
                ny = y+dy[1]
                nx = x+dx[1]
                arr[ny][nx] += 1
                y -= 1
                stack2.append(2)
            elif d == 2:
                ny = y+dy[2]
                nx = x+dx[2]
                arr[ny][nx] += 1
                x-=1
                stack2.append(3)
            elif d == 3:
                ny = y+dy[3]
                nx = x+dx[3]
                arr[ny][nx] += 1
                y+= 1
                stack2.append(0)
        
        check += 1
        if check != 0:
            stack = tmp + stack2
        else:
            stack = stack2

answer = 0
for y in range(100):
    for x in range(100):
        if arr[y][x] > 0 and arr[y][x+1] > 0 and arr[y+1][x] > 0 and arr[y+1][x+1] > 0:
            answer += 1

print(answer)




    
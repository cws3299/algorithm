import sys
sys.stdin = open('10806.txt','r')
from collections import deque
from copy import deepcopy

n,m,k,t = map(int, input().split())

dy = [-2,-2,-1,-1,1,1,2,2]
dx = [-1,1,-2,2,-2,2,-1,1]

arr = [[0]*n for _ in range(n)]
visit = [[-1]*n for _ in range(n)]
virus = deque()
confirm = deque()

cnt = 0
while cnt < m+k:
    try:
        if cnt < m:
            x,y = map(int, input().split())
            virus.append((y-1,x-1))
            visit[y-1][x-1] = 0
            arr[y-1][x-1] = 1
        if cnt >= m:
            x,y = map(int, input().split())
            confirm.append((y-1,x-1))
        cnt += 1
    except:
        break

day = 1
vl = len(virus)
while day <= t and vl > 0:
    for _ in range(vl):
        y,x = virus.popleft()
        for k in range(8):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<n:
                if visit[ny][nx] != 2:
                    if visit[ny][nx] == 0:
                        if day%2 == 1:
                            visit[ny][nx] = 2
                            arr[ny][nx] += 1
                            virus.append((ny,nx))
                    if visit[ny][nx] == 1:
                        if day%2 == 0:
                            visit[ny][nx] = 2
                            arr[ny][nx] += 1
                            virus.append((ny,nx))
                    if visit[ny][nx] == -1:
                        visit[ny][nx] = day%2
                        arr[ny][nx] += 1
                        virus.append((ny,nx))
    day += 1
    vl = len(virus)

tt = (t)%2
# print(visit)
flag = False
for c in confirm:
    y,x = c[0],c[1]
    if visit[y][x] == tt or visit[y][x] == 2:
        print("YES")
        flag = True
        break

if flag == False:
    print("NO")
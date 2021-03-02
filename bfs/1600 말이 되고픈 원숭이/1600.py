import sys
sys.stdin = open('1600.txt','r')
from collections import deque
from copy import deepcopy

def bfs():
    global kk,n,m,arr,visit,ans

    q = deque()
    q.append([0,0,0,0])
    visit[0][0][0] = 1

    if m == 1 and n == 1:
        ans = 0
        return 

    while q:
        y,x,h,move = q.popleft()

        if y == n-1 and x == m-1:
            ans = move
            break

        for k in range(8):
            ny = y+hy[k]
            nx = x+hx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 0 and h<kk:
                    if visit[ny][nx][h+1] == 0:
                        visit[ny][nx][h+1] = 1
                        q.append([ny,nx,h+1,move+1])
        
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 0:
                    if visit[ny][nx][h] == 0:
                        visit[ny][nx][h] = 1
                        q.append([ny,nx,h,move+1])

    return


hy = [-2,-2,-1,-1,1,1,2,2]
hx = [1,-1,2,-2,2,-2,1,-1]
dy = [0,0,-1,1]
dx = [1,-1,0,0]

kk = int(input())
m,n = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

visit = [[[0]*35 for _ in range(m)] for _ in range(n)]
ans = 100000
bfs()

if ans == 100000:
    print(-1)
else:
    print(ans)
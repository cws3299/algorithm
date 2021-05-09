import sys
sys.stdin = open('11567.txt','r')
from collections import deque

def bfs():
    global n,m,arr,sy,sx,ey,ex

    q = deque()
    q.append([sy,sx])

    while q:
        y,x = q.popleft()

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if not (ny == ey and  nx == ex):
                    if arr[ny][nx] == '.':
                        arr[ny][nx] = 'X'
                        q.append([ny,nx])
                else:
                    if arr[ny][nx] == '.':
                        arr[ny][nx] = 'X'
                        q.append([ny,nx])
                    else:
                        return False

    return True


dy = [0,0,-1,1]
dx = [1,-1,0,0]        

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(input())
    arr.append(arr1)

sy,sx = map(int, input().split())
ey,ex = map(int, input().split())

sy -= 1
sx -= 1
ey -= 1
ex -= 1


ss = bfs()

if ss == False:
    print('YES')
else:
    print('NO')
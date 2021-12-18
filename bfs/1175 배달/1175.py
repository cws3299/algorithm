import sys
sys.stdin = open('1175.txt','r')
from collections import deque

n,m = map(int,input().split())
arr = []
for _ in range(n):
    ar = list(input())
    arr.append(ar)

visit = [[[[0]*4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
c1_y, c1_x, c2_y, c2_x = None , None, None, None
sy,sx = None, None
dy = [0,0,-1,1]
dx = [-1,1,0,0]

for y in range(n):
    for x in range(m):
        if arr[y][x] == 'C' and c1_x == None:
            c1_y = y
            c1_x = x
            arr[y][x] = 'A'
        elif arr[y][x] == 'C' and c1_x != None:
            c2_y = y
            c2_x = x
            arr[y][x] = 'B'
        elif arr[y][x] == 'S':
            sy = y
            sx = x

answer = -1
q = deque()
q.append([sy,sx,0,-1,0])

while q:
    y,x,cnt,d,move = q.popleft()

    if cnt == 3:
        answer = move
        break

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if k != d:
                if arr[ny][nx] == '.' or arr[ny][nx] == 'S':
                    if visit[ny][nx][cnt][k] == 0:
                        visit[ny][nx][cnt][k] = 1
                        q.append([ny,nx,cnt,k,move+1])
                elif arr[ny][nx] == 'A':
                    if cnt == 0:
                        if visit[ny][nx][1][k] == 0:
                            visit[ny][nx][1][k] = 1
                            q.append([ny,nx,1,k,move+1])
                    elif cnt == 1:
                        if visit[ny][nx][1][k] == 0:
                            visit[ny][nx][1][k] = 1
                            q.append([ny,nx,1,k,move+1])
                    elif cnt == 2:
                        if visit[ny][nx][3][k] == 0:
                            visit[ny][nx][3][k] = 1
                            q.append([ny,nx,3,k,move+1])
                elif arr[ny][nx] == 'B':
                    if cnt == 0:
                        if visit[ny][nx][2][k] == 0:
                            visit[ny][nx][2][k] = 1
                            q.append([ny,nx,2,k,move+1])
                    elif cnt == 1:
                        if visit[ny][nx][3][k] == 0:
                            visit[ny][nx][3][k] = 1
                            q.append([ny,nx,3,k,move+1])
                    elif cnt == 2:
                        if visit[ny][nx][2][k] == 0:
                            visit[ny][nx][2][k] = 1
                            q.append([ny,nx,2,k,move+1])

print(answer)
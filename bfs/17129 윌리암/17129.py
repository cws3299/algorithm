import sys
sys.stdin = open('17129.txt','r')
from collections import deque

def bfs():
    global n,m,arr,birds,food1,food2,food3,answer,visit

    q = deque()
    visit[birds[0]][birds[1]] = 1
    q.append([0,birds[0],birds[1]])

    while q:
        cnt,y,x = q.popleft()

        if arr[y][x] == 3 or arr[y][x] == 4 or arr[y][x] == 5:
            answer = cnt
            break

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if visit[ny][nx] == 0:
                    if arr[ny][nx] != 1:
                        visit[ny][nx] = 1
                        q.append([cnt+1,ny,nx])


    return



dy = [0,0,-1,1]
dx = [1,-1,0,0]

n,m = map(int, input().split())
arr = []
for _ in range(n):
    ar = list(map(int,input()))
    arr.append(ar)

birds = None
food1 = None
food2 = None
food3 = None
answer = 0
visit = [[0]*m for _ in range(n)]


for y in range(n):
    for x in range(m):
        if arr[y][x] == 2:
            birds = [y,x]
        elif arr[y][x] == 3:
            food1 = [y,x]
        elif arr[y][x] == 4:
            food2 = [y,x]
        elif arr[y][x] == 5:
            food3 = [y,x]

bfs()

if answer == 0:
    print('NIE')
else:
    print('TAK')
    print(answer)
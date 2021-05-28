import sys
sys.stdin = open('5427.txt','r')
from collections import deque


def bfs2(y,x):
    global n,m,arr,sy,sx,fires,visit,answer

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if arr[ny][nx] == '*':
                return False
    
    return True

def bfs():
    global n,m,arr,sy,sx,fires,visit,answer

    visit[sy][sx] = 1
    q = deque()
    q.append([sy,sx,0])

    ll = len(q)
    ll2 = len(fires)
    while q:

        for _ in range(ll):
            y,x,move = q.popleft()

            for k in range(4):
                ny = y+dy[k]
                nx = x+dx[k]
                if 0<=ny<n and 0<=nx<m:
                    if arr[ny][nx] == '.' and visit[ny][nx] == 0:
                        result = bfs2(ny,nx)
                        if result == True:
                            visit[ny][nx] = 1
                            q.append([ny,nx,move+1])
                else:
                    answer = move+1
                    return

        for _ in range(ll2):
            y,x = fires.popleft()
            for k in range(4):
                ny = y+dy[k]
                nx = x+dx[k]
                if 0<=ny<n and 0<=nx<m:
                    if arr[ny][nx] == '.':
                        arr[ny][nx] = '*'
                        fires.append([ny,nx])

        ll = len(q)
        ll2 = len(fires)
        
    return



dy = [0,0,-1,1]
dx = [1,-1,0,0]    

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    arr = []
    for _ in range(n):
        arr1 = list(input())
        arr.append(arr1)

    sy,sx = None , None
    fires = deque()

    for y in range(n):
        for x in range(m):
            if arr[y][x] == '@':
                sy = y
                sx = x
            elif arr[y][x] == '*':
                fires.append([y,x])

    visit = [[0]*m for _ in range(n)]

    answer = None
    bfs()

    if answer == None:
        print('IMPOSSIBLE')
    else:
        print(answer)
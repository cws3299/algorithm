import sys
sys.stdin = open('14500.txt','r')
sys.setrecursionlimit(10**5)
from collections import deque

def dfs(y,x,many,cnt):
    global n,m,arr,answer,visit

    if many == 4:
        if answer < cnt:
            answer = cnt
        return

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                many += 1
                cnt += arr[ny][nx]
                dfs(ny,nx,many,cnt)
                visit[ny][nx] = 0
                many -= 1
                cnt -= arr[ny][nx]

    return

def bfs(y,x,cnt,b):
    global dy,dx,n,m,arr,answer

    q = deque()
    q.append([y,x])
    ans = cnt

    ct = 0
    while ct < 1:
        y,x = q.popleft()

        stop = 0
        for k in b:
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                stop += 1
                ans += arr[ny][nx]


        if stop == 3:
            if ans > answer:
                answer = ans

        
        ct += 1

    return


    
dy = [-1,1,0,0]
dx = [0,0,-1,1]

n,m = map(int, input().split())

arr= []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

answer = 0

visit = [[0]*m for _ in range(n)]

for y in range(n):
    for x in range(m):
        visit[y][x] = 1
        dfs(y,x,1,arr[y][x])
        visit[y][x] = 0


bfs3 = [0,1,2]
bfs2 = [0,1,3]
bfs1 = [0,2,3]
bfs0 = [1,2,3]

for y in range(n):
    for x in range(m):
        bfs(y,x,arr[y][x],bfs0)
        bfs(y,x,arr[y][x],bfs1)
        bfs(y,x,arr[y][x],bfs2)
        bfs(y,x,arr[y][x],bfs3)


print(answer)
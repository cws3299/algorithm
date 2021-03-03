import sys
sys.stdin = open('2146.txt','r')
from collections import deque
sys.setrecursionlimit(10**5)
import heapq

def setting(cn,y,x):
    global n,arr,visit,lands

    q = deque()
    q.append([y,x])
    visit[y][x] = 1
    lands[y][x] = cn

    while q:
        y,x = q.popleft()

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<n:
                if visit[ny][nx] == 0 and arr[ny][nx] == 1:
                    visit[ny][nx] = 1
                    lands[ny][nx] = cn
                    q.append([ny,nx])

    return

def bfs(y,x,me):
    global n,arr,visit,lands,ans,confirm

    pq = []
    heapq.heappush(pq,[0,y,x])
    visit[y][x] = 1
    confirm[y][x] = 1

    while pq:
        cnt,y,x = heapq.heappop(pq)

        if lands[y][x] != 0 and lands[y][x] != me:
            if ans > cnt:
                ans = cnt
            break

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<n:
                if lands[ny][nx] == me:
                    visit[ny][nx] = 1
                if confirm[ny][nx] == 0:
                    confirm[ny][nx] = 1
                    if lands[ny][nx] == 0:
                        heapq.heappush(pq,[cnt+1,ny,nx])
                    if lands[ny][nx] == me:
                        heapq.heappush(pq,[cnt,ny,nx])
                    if lands[ny][nx] != 0 and lands[ny][nx] != me:
                        heapq.heappush(pq,[cnt,ny,nx])

    return


dy = [0,0,-1,1]
dx = [1,-1,0,0]

n = int(input())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

visit = [[0]*n for _ in range(n)]
lands = [[0]*n for _ in range(n)]
confirm = [[0]*n for _ in range(n)]

cn = 1
for y in range(n):
    for x in range(n):
        if arr[y][x] == 1 and visit[y][x] == 0:
            setting(cn,y,x)
            cn += 1
ans = 10000

visit = [[0]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if visit[y][x] == 0 and lands[y][x] != 0:
            bfs(y,x,lands[y][x])
            confirm = [[0]*n for _ in range(n)]


print(ans)
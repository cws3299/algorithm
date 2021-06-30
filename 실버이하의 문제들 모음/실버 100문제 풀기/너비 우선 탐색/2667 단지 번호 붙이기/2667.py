import sys
sys.stdin = open('2667.txt')
from collections import deque

def bfs(y,x):
    global n,arr,visit,answer

    q = deque()
    q.append([y,x])
    visit[y][x] = 1
    res = 1

    while q:
        y,x = q.popleft()

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<n:
                if arr[ny][nx] == 1:
                    if visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        res += 1
                        q.append([ny,nx])

    return res


dy = [0,0,-1,1]
dx = [1,-1,0,0]

n = int(input())
arr = []
for _ in range(n):
    ar = list(map(int,input()))
    arr.append(ar)

visit = [[0]*n for _ in range(n)]

answer = []

for y in range(n):
    for x in range(n):
        if arr[y][x] == 1 and visit[y][x] == 0:
            result = bfs(y,x)
            answer.append(result)


answer.sort()

print(len(answer))
for ans in answer:
    print(ans)
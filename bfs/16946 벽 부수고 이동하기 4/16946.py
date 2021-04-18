import sys
sys.stdin = open('16946.txt','r')
from collections import deque

def setting(y,x,ct):
    global n,m,arr,visit,plus,number

    q = deque()
    lst = deque()
    q.append([y,x,ct])
    lst.append([y,x,ct])
    visit[y][x] = 1

    result = 1

    while q:
        y,x,ct = q.popleft()

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 0 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    result += 1
                    q.append([ny,nx,ct])
                    lst.append([ny,nx,ct])

    while lst:
        y,x,ct = lst.popleft()

        visit[y][x] = 1
        number[y][x] = ct
        plus[y][x] = result

    return

def confirm(y,x):
    global n,m,arr,visit,plus,number,answer

    result = 1

    lst = []

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if number[ny][nx] not in lst:
                lst.append(number[ny][nx])
                result += plus[ny][nx]

    answer[y][x] = result%10

    return

dy = [-1,1,0,0]
dx = [0,0,-1,1]

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(map(int, input()))
    arr.append(arr1)

visit = [[0]*m for _ in range(n)]
plus = [[0]*m for _ in range(n)]
number = [[0]*m for _ in range(n)]
answer = [[0]*m for _ in range(n)]

cnt = 1
for y in range(n):
    for x in range(m):
        if arr[y][x] == 0 and visit[y][x] == 0:
            setting(y,x,cnt)
            cnt += 1

for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            confirm(y,x)

for ans in answer:
    for an in ans:
        print(an, end = '')
    print()
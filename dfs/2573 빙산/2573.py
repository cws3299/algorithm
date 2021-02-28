import sys
sys.stdin = open('2573.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy
from collections import deque

def melting(y,x):
    global n,m,arr,total,temp


    cnt = 0
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if arr[ny][nx] == 0:
                cnt += 1

    temp[y][x] = arr[y][x]-cnt

    if temp[y][x] <=0 :
        temp[y][x] = 0
        total -= 1

    return

def confirm(y,x):
    global n,m,arr,total,temp

    q = deque()
    q.append([y,x])
    visit[y][x] = 1

    ct = 1 

    while q:
        y,x = q.popleft()

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if visit[ny][nx] == 0 and arr[ny][nx]>0:
                    visit[ny][nx] = 1
                    ct += 1
                    q.append([ny,nx])
        
    
    return ct


dy = [0,0,-1,1]
dx = [1,-1,0,0]
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

total = 0
temp = deepcopy(arr)
visit = [[0]*m for _ in range(n)] 

for y in range(n):
    for x in range(m):
        if arr[y][x] != 0:
            total += 1


cnt = 1
ans = 10
stopp = False
while True:
    for y in range(n):
        for x in range(m):
            if arr[y][x] != 0:
                melting(y,x)
    arr = deepcopy(temp)
    temp = deepcopy(arr)
    for y in range(n):
        for x in range(m):
            if arr[y][x] != 0:
                two = confirm(y,x)
                visit = [[0]*m for _ in range(n)] 
                stopp = True
                break
        if stopp == True:
            break

    if two < total:
        break
    
    if two <=1 and two == total:
        ans = 0
        break
    

    cnt += 1
    stopp = False

    


if ans == 0:
    print(ans)
else:
    print(cnt)
    
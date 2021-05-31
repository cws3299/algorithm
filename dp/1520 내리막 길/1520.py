import sys
sys.stdin = open('1520.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy

def go(y,x,v):
    global n,m,arr,dp,visit

    if y == n-1 and x == m-1:
        dp[y][x] = 1
        return dp[y][x]

    if dp[y][x] != 0 or visit[y][x] !=0:
        return dp[y][x]

    flag = False
    for k in range(4):
        if k == 0:
            ny = y-1
            nx = x
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] < v:
                    flag = True
                    dp[y][x] += go(ny,nx,arr[ny][nx])
        if k == 1:
            ny = y+1
            nx = x
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] < v:
                    flag = True
                    dp[y][x] += go(ny,nx,arr[ny][nx])
        if k == 2:
            ny = y
            nx = x-1
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] < v:
                    flag = True
                    dp[y][x] += go(ny,nx,arr[ny][nx])
        if k == 3:
            ny = y
            nx = x+1
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] < v:
                    flag = True
                    dp[y][x] += go(ny,nx,arr[ny][nx])
                    
        if flag == False:
            visit[y][x] = 1


    return dp[y][x]

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

dp = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]

go(0,0,arr[0][0])

print(dp[0][0])
import sys
sys.stdin = open('1937.txt','r')
sys.setrecursionlimit(10**5)

def go(y,x):
    global n,arr,dp

    if dp[y][x] != 0:
        return dp[y][x]

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<n:
            if arr[ny][nx] > arr[y][x]:
                dp[y][x] = max(go(ny,nx)+1, dp[y][x])

    return dp[y][x]


dy = [0,0,-1,1]
dx = [1,-1,0,0]
n = int(input())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

dp = [[0]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        go(y,x)

answer = 0
for y in range(n):
    for x in range(n):
        if dp[y][x] > answer:
            answer = dp[y][x]

# print(dp)
print(answer+1)
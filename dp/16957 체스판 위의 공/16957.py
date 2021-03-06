import sys
sys.stdin = open('16957.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy

def go(sy,sx,y,x,v):
    global n,m,arr,dp,visit,plus


    nxt_x = x
    nxt_y = y
    nxt_num = arr[y][x]
    # print(y,x)
    for k in range(8):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if arr[ny][nx] < nxt_num:
                # print(ny,nx,1111111111111111)
                nxt_num = arr[ny][nx]
                nxt_x = nx
                nxt_y = ny

    # if nxt_y == y and nxt_x == x:


    # return

    if nxt_y == y and nxt_x == x:
        # print('===============================================================')
        plus[dp[nxt_y][nxt_x]] += 1
        return dp[y][x]

### save

    # print('[---',y,x,nxt_y,nxt_x,nxt_num)
    if dp[nxt_y][nxt_x] == arr[y][x]:
        if 0<=nxt_y<n and 0<=nxt_x<m:
            visit[nxt_y][nxt_x] = 1
            plus[dp[nxt_y][nxt_x]] += 1
            dp[y][x] = dp[nxt_y][nxt_x]
            return dp[y][x]
    else:
        if 0<=nxt_y<n and 0<=nxt_x<m:
            if visit[nxt_y][nxt_x] == 0:
                visit[nxt_y][nxt_x] = 1
                result = go(sy,sx,nxt_y,nxt_x,v+1)
                # print('++++')
                dp[y][x] = deepcopy(result)
                return dp[y][x]
            if visit[nxt_y][nxt_x] == 1:
                plus[dp[nxt_y][nxt_x]] += 1
                dp[y][x] = dp[nxt_y][nxt_x]
                return dp[y][x]

    return dp[y][x]



        


dy = [1,1,1,0,0,-1,-1,-1]
dx = [-1,0,1,-1,1,-1,0,1]
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

dp = deepcopy(arr) # 변경된 수
visit = [[0]*m for _ in range(n)] # 방문 여부
plus = {i:0 for i in range(300001)}

# print(plus)

for y in range(n):
    for x in range(m):
        go(y,x,y,x,1)
        # print('----------------------',y,x,dp,plus)

for y in range(n):
    for x in range(m):
        if dp[y][x] != 0:
            dp[y][x] += 1
            

# print(dp)
# print(plus)
for y in range(n):
    for x in range(m):
        print(plus[arr[y][x]], end= ' ')
    print()
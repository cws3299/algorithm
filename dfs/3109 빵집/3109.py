import sys
sys.stdin = open('3109.txt','r')
sys.setrecursionlimit(10**5)

def dfs(y,x):
    global n,m,arr,visit,answer,flag

    # print(y,x)

    if x == m-1:
        answer += 1
        flag = False
        return

    for k in range(3):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if flag == True:
                if arr[ny][nx] == '.':
                    if visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        dfs(ny,nx)

    return

dy = [-1,0,1]
dx = [1,1,1]

n,m = map(int, input().split())
arr = []
for _ in range(n):
    ar = list(input())
    arr.append(ar)

visit = [[0]*m for _ in range(n)]

answer = 0

for k in range(n):
    flag = True
    dfs(k,0)
    # print('-----------------------------------------------')

print(answer)
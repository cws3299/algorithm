import sys
sys.stdin = open('16929.txt','r')
sys.setrecursionlimit(10**5)

def dfs(y,x,py,px,color,move):
    global n,m,arr,visit,ans,check

    # print(y,x,py,px,color,move)

    if check[y][x] == 1 and move >3 and arr[y][x] == color :
        ans = True
        # print(ans)
        return

    check[y][x] = 1

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if arr[ny][nx] == color:
                if not (ny == py and nx == px):
                    # check[ny][nx] = 1
                    visit[ny][nx] = 1
                    move += 1
                    dfs(ny,nx,y,x,color,move)
                    move -= 1
                    # check[ny][nx] = 0

    return

        

dy = [0,0,-1,1]
dx = [1,-1,0,0]

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(input())
    arr.append(arr1)

visit = [[0]*m for _ in range(n)]
check = [[0]*m for _ in range(n)]
ans = False
answer = False
stop = False
for y in range(n):
    for x in range(m):
        if visit[y][x] == 0:
            visit[y][x] = 1
            check[y][x] = 1
            dfs(y,x,y,x,arr[y][x],0)
            check = [[0]*m for _ in range(n)]
            # print('--------------',ans)
            if ans == True:
                answer = True
                stop = True
                break
    if stop == True:
        break

if answer == False:
    print('No')
else:
    print('Yes')

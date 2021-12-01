[ 백준 : 마알 ] (https://www.acmicpc.net/problem/1795)



- 취업하고 알고리즘을 한동안 안했더니.... 시간이 엄청 오래걸렸다
- 코드의 핵심은 여러가지인데 일단 개인적으로 그 중 하나만 적어보자면 bfs는 마알 하나 기준 bfs2는 각 bfs의 마알이 k번만큼 이동하는 것
- bfs2의 경우에 visit체크를 신경써서 해줘야한다.



```python
import sys
sys.stdin = open('1795.txt','r')
from collections import deque

def bfs(mal,panCnt):
    global n,m,arr,mals,final,visit

    c,sy,sx = mal[0],mal[1],mal[2]

    q = deque()
    bfsCnt = 0
    q.append([c,sy,sx,bfsCnt])
    visit[sy][sx][sy][sx] = bfsCnt
    arrCnt = 1

    while q:
        c,y,x,cnt = q.popleft()

        results = bfs2(cnt,c,y,x)

        for result in results:
            if visit[sy][sx][result[1]][result[2]] > result[3]:
                visit[sy][sx][result[1]][result[2]] = result[3]
                arrCnt += 1
                q.append([c,result[1],result[2],result[3]])


    return



def bfs2(bfsCnt,c,sy,sx):
    global n,m,arr,mals,final,visit

    evenBfsViist = [[-1]*m for _ in range(n)]
    oddBfsViist = [[-1]*m for _ in range(n)]

    q = deque()
    q.append((0,sy,sx,bfsCnt+1))
    evenBfsViist[sy][sx] = 0

    check = 0
    if c % 2 == 1:
        check = 1

    while q:

        move,y,x,cnt = q.popleft()

        if move == c:
            q.append((move,y,x,cnt))
            break

        for k in range(8):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if (move+1) % 2 == 0:
                    if evenBfsViist[ny][nx] == -1:
                        evenBfsViist[ny][nx] = move+1
                        q.append((move+1,ny,nx,cnt))
                else:
                    if oddBfsViist[ny][nx] == -1:
                        oddBfsViist[ny][nx] = move+1
                        q.append((move+1,ny,nx,cnt))


    q = deque()

    for y in range(n):
        for x in range(m):
            if oddBfsViist[y][x] != -1:
                q.append([oddBfsViist[y][x],y,x,bfsCnt+1])
    # q.append([evenBfsViist[sy][sx],sy,sx,bfsCnt+1])
    for y in range(n):
        for x in range(m):
            if evenBfsViist[y][x] != -1:
                q.append([evenBfsViist[y][x],y,x,bfsCnt+1])

    return q





dy = [1,1,2,2,-1,-1,-2,-2]
dx = [-2,2,-1,1,-2,2,-1,1]

n,m = map(int,input().split())
arr = []
mals = []
panCnt = 0
for _ in range(n):
    ar = list(input())
    arr.append(ar)

for y in range(n):
    for x in range(m):
        if arr[y][x] != '.':
            arr[y][x] = int(arr[y][x])
            mals.append([arr[y][x],y,x])
        panCnt += 1

final = [[0]*m for _ in range(n)]
visit = [[[[float('inf')]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
answer = 1000000

can = [[0]*m for _ in range(n)]

if len(mals) == 1:
    print(0)
else:
    for mal in mals:
        bfs(mal,panCnt)

    for y in range(n):
        for x in range(m):
            for yy in range(n):
                for xx in range(m):
                    if arr[y][x] != '.' and visit[y][x][yy][xx] != float('inf'):
                        final[yy][xx] += visit[y][x][yy][xx]
                        can[yy][xx] += 1

    for y in range(n):
        for x in range(m):
            if answer > final[y][x] and can[y][x] == len(mals):
                answer = final[y][x]

    if answer == 1000000:
        print(-1)
    else:
        print(answer)
```

![20211109_215434](20211109_215434.png)


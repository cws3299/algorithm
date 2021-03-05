import sys
sys.stdin = open('16959.txt','r')
from collections import deque
import heapq

def bfs():
    global n,arr,visit,sy,sx,ans

    # q = deque()
    # q.append([sy,sx,1,0,1])
    # q.append([sy,sx,1,1,1])
    # q.append([sy,sx,1,2,1])
    pq = []
    heapq.heappush(pq,[0,sy,sx,1,0])
    heapq.heappush(pq,[0,sy,sx,1,1])
    heapq.heappush(pq,[0,sy,sx,1,2])
    # visit[sy][sx][1][0][0] = 1
    # visit[sy][sx][1][1] = 1
    # visit[sy][sx][1][2] = 1

    while pq:
        cnt,y,x,now,chess = heapq.heappop(pq)

        # print(cnt,y,x,now,chess)

        if arr[y][x] == n*n and now == n*n:
            ans = cnt
            break

        for ss in range(3):
            if ss == 0:
                for k in range(8):
                    ny = y+dy[k]
                    nx = x+dx[k]
                    if 0<=ny<n and 0<=nx<n:
                        if visit[ny][nx][now][ss][chess] == 0:
                            visit[ny][nx][now][ss][chess] = 1
                            if arr[ny][nx] == now+1:
                                if chess == ss:
                                    heapq.heappush(pq,[cnt+1,ny,nx,now+1,0])
                                else:
                                    heapq.heappush(pq,[cnt+2,ny,nx,now+1,0])
                            else:
                                if chess == ss:
                                    heapq.heappush(pq,[cnt+1,ny,nx,now,0])
                                else:
                                    heapq.heappush(pq,[cnt+2,ny,nx,now,0])
            elif ss == 1:
                cntt = 1
                stop = True
                while stop:
                    kk = 0

                    for k in range(4):
                        ny = y+by[k]*cntt
                        nx = x+bx[k]*cntt
                        if 0<=ny<n and 0<=nx<n:
                            if visit[ny][nx][now][ss][chess] == 0:
                                visit[ny][nx][now][ss][chess] = 1
                                if arr[ny][nx] == now+1:
                                    if chess == ss:
                                        heapq.heappush(pq,[cnt+1,ny,nx,now+1,1])
                                    else:
                                        heapq.heappush(pq,[cnt+2,ny,nx,now+1,1])
                                else:
                                    if chess == ss:
                                        heapq.heappush(pq,[cnt+1,ny,nx,now,1])
                                    else:
                                        heapq.heappush(pq,[cnt+2,ny,nx,now,1])
                        else:
                            kk += 1
                        
                    if kk == 4:
                        stop = False
                    kk = 0
                    

                    cntt += 1
            elif ss == 2:
                cntt = 1
                stop = True
                # print('-----')
                while stop:
                    kk = 0
                    for k in range(4):
                        ny = y+ry[k]*cntt
                        nx = x+rx[k]*cntt
                        if 0<=ny<n and 0<=nx<n:
                            # print(ny,nx,visit[ny][nx][now])
                            if visit[ny][nx][now][ss][chess] == 0:
                                visit[ny][nx][now][ss][chess] = 1
                                # print('------------',ny,nx,now,chess)
                                if arr[ny][nx] == now+1:
                                    if chess == ss:
                                        heapq.heappush(pq,[cnt+1,ny,nx,now+1,2])
                                    else:
                                        heapq.heappush(pq,[cnt+2,ny,nx,now+1,2])
                                else:
                                    if chess == ss:
                                        heapq.heappush(pq,[cnt+1,ny,nx,now,2])
                                    else:
                                        heapq.heappush(pq,[cnt+2,ny,nx,now,2])
                        else:
                            kk += 1

                    if kk == 4:
                        stop = False
                    kk = 0

                    cntt += 1
        
    return
        

                    


dy = [-2,-2,-1,-1,1,1,2,2]
dx = [1,-1,2,-2,2,-2,1,-1]

by = [-1,-1,1,1]
bx = [1,-1,1,-1]

ry = [0,0,1,-1]
rx = [1,-1,0,0]

ans= 0
n = int(input())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

visit = [[[[[0]*3 for _ in range(3)] for _ in range((n*n)+1)] for _ in range(n)]for _ in range(n)]

sy,sx = None,None

for y in range(n):
    for x in range(n):
        if arr[y][x] == 1:
            sy = y
            sx = x

bfs()

print(ans)
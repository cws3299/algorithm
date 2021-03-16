import sys
sys.stdin = open('2665.txt','r')
import heapq

def bfs():
    global n,arr,pan

    pq = []
    heapq.heappush(pq,[0,0,0])
    pan[0][0] = 0

    while pq:
        cnt,y,x, = heapq.heappop(pq)

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<n:
                # print(ny,nx)
                if pan[ny][nx] == -1:
                    if arr[ny][nx] == 1:
                        pan[ny][nx] = cnt
                        heapq.heappush(pq,[cnt,ny,nx])
                    else:
                        pan[ny][nx] = cnt + 1
                        heapq.heappush(pq,[cnt+1,ny,nx])

    # print(pan)

    return pan[n-1][n-1]

                    


dy = [-1,1,0,0]
dx = [0,0,-1,1]

n = int(input())
arr = []
for _ in range(n):
    arr1 = list(map(int, input()))
    arr.append(arr1)

pan = [[-1]*n for _ in range(n)]
print(bfs())
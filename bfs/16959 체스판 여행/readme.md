[백준 16959:체스판 여행] (https://www.acmicpc.net/problem/16959)



### 구현과정에서 상당히 힘들었던 문항



- 답을 구하는 과정에서 자꾸 예제에서 틀린답이 발생했다.
- 결국 방문배열을 5차원이라는 엄청 크게 만들어서 문제를 해결했다. 메모리 제한이 있는 문제에서는 쉽지 않을 것 같다.
- 정말 코딩은 어려운것 같다. 하지만 재밌다!!!!!!



2021.03.06



```python
import sys
sys.stdin = open('16959.txt','r')
import heapq

def bfs():
    global n,arr,visit,sy,sx,ans

    pq = []
    heapq.heappush(pq,[0,sy,sx,1,0])
    heapq.heappush(pq,[0,sy,sx,1,1])
    heapq.heappush(pq,[0,sy,sx,1,2])

    while pq:
        cnt,y,x,now,chess = heapq.heappop(pq)

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
```



![20210306_021337](20210306_021337.png)
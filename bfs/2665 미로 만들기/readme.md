[백준 : 미로만들기] (https://www.acmicpc.net/problem/2665)



- 예전에 풀지 못했던 문제라 약간 긴장한채로 문제를 풀었는데 너무 쉽게 풀려서 당황스러운 문제
- 로직
  - arr배열에 미로자체를 넣는다.
  - 같은 크기의 pan이라는 배열을 만든다. pan배열에는 해당 위치를 가기위해 몇개를 부숴야하는지에 대한 값을 넣어주는 배열이다
  - heapq를 통해 부숴준 값이 적은 순서대로 미로를 4방탐색하면서 이동해야할 방이 흰방일 경우 cnt를 그대로 넣어서 heapq에 넣고 까만방일 경우 cnt+1을 해서 heapq에 값을 넣어준다. 이 과정을 반복한 후 결과적으로 끝방의 pan배열 값을 출력한다



2021.03.16에 풀기시작해서 딱 03.17이 되면서 풀었다



```python
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
```

![20210317_000829](20210317_000829.png)
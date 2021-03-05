[백준 - 2176: 합리적인 이동경로] (https://www.acmicpc.net/problem/2176)



#### 너무 빠르게 정답을 맞춰서 뭔가 당황스럽다. 뭐지.....???

- 로직 
  - 1.  다익스트라로 2위치에서 각 위치까지의 거리들을 answer 배열에 저장
    2. 1위치에서 dp를 돌린다. 목적지는 2!!!!!!
       - 다만 조건은 다음 위치에서 2까지의 거리가 현재 위치에서 2까지의 거리보다 가까운 경우만 넣어주기



2021.03.05



```python
import sys
sys.stdin = open('2176.txt','r')
sys.setrecursionlimit(10**5)
import heapq

def dijkstra():
    global n,m,answer,roads

    pq = []
    answer[2] = 0
    heapq.heappush(pq,[answer[2],2])

    while pq:
        now_distance, now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt , wt in roads[now_position].items():
            distance = now_distance+wt

            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return

def go(now,distance):
    global n,m,answer,roads,dp

    if now == 2:
        return 1

    if dp[now] != 0:
        return dp[now]

    for nxt in roads[now].keys():
        if answer[nxt] < distance:
            dp[now] += go(nxt,answer[nxt])

    return dp[now]


n,m = map(int, input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(m):
    s,e,w = map(int, input().split())
    roads[s][e] = w
    roads[e][s] = w

answer = [float('inf')]*(n+1)

dijkstra()

dp = [0]*(n+1)

# print(roads)
# print(answer)
go(1,answer[1])

# print(dp)
print(dp[1])
```



![20210305_121931](20210305_121931.png)
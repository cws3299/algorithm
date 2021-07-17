[백준 : 정복자] (https://www.acmicpc.net/problem/14950)



- 일반적인 mst문제
- t에 관련된 값의 경우 result2라는 변수를 따로 만들어서 관리했다.



```python
import sys
sys.stdin = open('14950.txt','r')
import heapq

n,m,t = map(int,input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(m):
    a,b,w = map(int, input().split())
    value = roads.get(a)
    vv = value.get(b)
    if vv == None or vv > w:
        roads[a][b] = w
        roads[b][a] = w

cnt = -1
answer = [float('inf')] * (n+1)
mst = [0] * (n+1)
pq = []
answer[1] = 0
heapq.heappush(pq,[answer[1],1])
result = 0
result2 = t

while pq:
    now_distance ,now_position = heapq.heappop(pq)

    if mst[now_position] != 0:
        continue

    mst[now_position] = 1
    result2 += cnt*t
    # print(result2)
    result += now_distance
    cnt += 1

    for nxt , wt in roads[now_position].items():
        if mst[nxt] == 0 and answer[nxt] > wt:
            answer[nxt] = wt
            heapq.heappush(pq,[answer[nxt],nxt])


print(result+result2) 


```

![20210716_154537](20210716_154537.png)
[백준 : 문제집] (https://www.acmicpc.net/problem/1766)



- 위상정렬 문제
- 위상이 0인경우 숫자가 작은 문제를 먼저 풀어야 하는 점을 해결하기 위해 heapq를 사용했다.



```python
import sys
sys.stdin = open('1766.txt','r')
import heapq

n,m = map(int, input().split())
indegree = [0]*(n+1)
arr = [[] for _ in range(n+1)]

for k in range(m):
    a,b = map(int, input().split())
    indegree[b] += 1
    arr[a].append(b)

pq = []

for k in range(1,n+1):
    if indegree[k] == 0:
        heapq.heappush(pq,k) 

while pq:
    now = heapq.heappop(pq)

    for nxt in arr[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(pq,nxt)

    print(now, end = ' ')
```

![20210701_105250](20210701_105250.png)
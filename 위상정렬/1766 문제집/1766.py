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
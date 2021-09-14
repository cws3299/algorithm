import sys
sys.stdin = open('2109.txt','r')

import heapq

n = int(input())
pq = []
arr = []
for _ in range(n):
    money , day = map(int, input().split())
    arr.append([day,money])

arr.sort()

for day , money in arr:
    heapq.heappush(pq,money)
    if day < len(pq):
        heapq.heappop(pq)

print(sum(pq))
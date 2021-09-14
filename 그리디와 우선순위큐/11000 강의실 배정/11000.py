import sys
sys.stdin = open('11000.txt','r')
import heapq
from collections import deque

n = int(input())
pq = []
for _ in range(n):
    s,e = map(int, input().split())
    pq.append([s,e])
    # heapq.heappush(pq,[s,e])
pq.sort(key=lambda x:(x[0],x[1]))
pq = deque(pq)


rooms = [1]
tq = []
answer = 0

while pq:
    start,end = pq.popleft()

    while tq and tq[0][0] <= start:
        ed, ss = heapq.heappop(tq)
        rooms[ss] = 0 
        
    sss = rooms.index(0)

    if sss > answer:
        answer = sss

    rooms[sss] = 1
    heapq.heappush(tq,[end,sss])

print(answer + 1)

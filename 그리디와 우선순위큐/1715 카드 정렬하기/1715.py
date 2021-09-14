import sys
sys.stdin = open('1715.txt','r')
import heapq

n = int(input())
pq = []
answer = 0
for _ in range(n):
    a = int(input())
    heapq.heappush(pq,a)

while len(pq) > 1:
    output1 = heapq.heappop(pq)
    output2 = heapq.heappop(pq)
    innput = output1 + output2
    answer += innput
    heapq.heappush(pq,innput)

print(answer)


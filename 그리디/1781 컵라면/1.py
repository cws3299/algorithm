import sys
sys.stdin = open('1781.py','r')
import heapq

n = int(input())
days = []
days.append([0,0])
pq = []
tq = []

for k in range(1,n+1):
    d,c = map(int,input().split())
    days.append([d,c])
    heapq.heappush(pq,[d,c])

answer = 0 

day = 1
while day <= pq[0][0]:
    d,c = heapq.heappop(pq)

    heapq.heappush(tq,[d,c])
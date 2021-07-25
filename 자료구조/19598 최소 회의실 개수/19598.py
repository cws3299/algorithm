import sys
sys.stdin = open('19598.txt','r')
input = sys.stdin.readline
import heapq

n = int(input())
pq = []

for s in range(1,n+1):
    start,end = map(int, input().split())
    heapq.heappush(pq,[start,end,s])

rooms = [0]*100001

tq = []
answer = 0

while pq:
    start,end,number = heapq.heappop(pq)

    while tq and tq[0][0] <= start:
        t_end , t_number = heapq.heappop(tq)
        index = rooms.index(t_number)
        rooms[index] = 0

    result = rooms.index(0)
    rooms[result] = number
    if result > answer:
        answer = result

    heapq.heappush(tq,[end,number])

print(answer+1)

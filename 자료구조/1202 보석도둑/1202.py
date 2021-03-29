import sys
sys.stdin = open('1202.txt','r')
import heapq

n,m = map(int,input().split())
pq = []
for _ in range(n):
    jewel = list(map(int, input().split()))
    heapq.heappush(pq,[jewel[0],jewel[1]])


answer = 0
bq = []
for k in range(m):
    bag = int(input())
    heapq.heappush(bq,[bag,k])

cnt = 0
ll = len(bq)
temp = []
while cnt < ll:
    bag_weight, bag_number = heapq.heappop(bq)

    ll2 = len(pq)
    cn = 0

    while pq and bag_weight >= pq[0][0]:
        [weight, value] = heapq.heappop(pq)
        heapq.heappush(temp, -value)

    if temp:
        answer -= heapq.heappop(temp)
    elif len(pq) == 0:
        break

    cnt += 1


print(answer) 


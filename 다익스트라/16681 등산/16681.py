import sys
sys.stdin = open('16681.txt','r')
import heapq

n,m,d,e = map(int, input().split())
height = [0] + list(map(int, input().split()))

road = {road:{} for road in range(n+1)}

for _ in range(m):
    a,b,w = map(int, input().split())
    value = road.get(a)
    vv = value.get(b)
    if vv == None or vv > w:
        road[a][b] = w
        road[b][a] = w


result1 = [float('inf')]* (n+1)
result2 = [float('inf')]* (n+1)

pq = []
result1[1] = 0
heapq.heappush(pq,[result1[1],height[1],1])

while pq:
    now_distance , now_height, now_position = heapq.heappop(pq)

    if result1[now_position] < now_distance:
        continue

    for nxt,wt in road[now_position].items():
        distance = now_distance + wt
        if result1[nxt] > distance and height[nxt] > now_height:
            result1[nxt] = distance
            heapq.heappush(pq,[distance,height[nxt],nxt])


pq = []
result2[n] = 0
heapq.heappush(pq,[result2[n],height[n],n])

while pq:
    now_distance , now_height, now_position = heapq.heappop(pq)

    if result2[now_position] < now_distance:
        continue

    for nxt,wt in road[now_position].items():
        distance = now_distance + wt
        if result2[nxt] > distance and height[nxt] > now_height:
            result2[nxt] = distance
            heapq.heappush(pq,[distance,height[nxt],nxt])

happy = -float('inf')
for k in range(1,n+1):
    if result1[k] != float('inf') and result2[k] != float('inf'):
        now = (height[k]*e) - ( (result1[k] + result2[k]) * d )
        if happy < now:
            happy = now

if happy == -float('inf'):
    print('Impossible')
else:
    print(happy)
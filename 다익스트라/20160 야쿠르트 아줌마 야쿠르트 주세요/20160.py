import sys
sys.stdin = open('20160.txt','r')
import heapq

def dijkstra(e):
    global n,m,roads,orders,times,ct

    start = orders[e-1-ct]
    end = orders[e]
    answer = [float('inf')]*(n+1)
    answer[start] = 0
    pq = []
    heapq.heappush(pq,[answer[start],start])

    while pq:
        now_distance,now_position = heapq.heappop(pq)

        if now_position == end:
            return now_distance

        if answer[now_position] < now_distance:
            continue

        for nxt, wt in roads[now_position].items():
            distance = now_distance + wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return False


def dijkstra_me(me):
    global n,m,roads,orders,times,ct

    answer = [float('inf')]*(n+1)
    answer[me] = 0
    pq = []
    heapq.heappush(pq,[answer[me],me])

    while pq:
        now_distance,now_position = heapq.heappop(pq)


        if answer[now_position] < now_distance:
            continue

        for nxt, wt in roads[now_position].items():
            distance = now_distance + wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    result = []

    for o in orders:
        if answer[o] != float('inf'):
            result.append(answer[o])
        else:
            result.append(None)

    return result

n,m = map(int, input().split())
roads = {i:{} for i in range(n+1)}

for _ in range(m):
    a,b,w = map(int,input().split())
    value = roads.get(a)
    vv = value.get(b)
    if vv == None or vv > w:
        roads[a][b] = w
        roads[b][a] = w

orders = list(map(int, input().split()))
me = int(input())

times = [0]

cnt = 1
ct = 0

while cnt <= 9:
    result = dijkstra(cnt)
    if result == False:
        times.append(None)
        ct += 1
    else:
        times.append(result)
        ct = 0

    cnt += 1

cart = []
a = 0
for k in times:
    if k != None:
        a += k
        cart.append(a)
    else:
        cart.append(None)

result = dijkstra_me(me)

answer = float('inf')
for k in range(10):
    if result[k] != None and cart[k] != None:
        if result[k] <= cart[k]:
            if orders[k] < answer:
                answer = orders[k]

if answer == float('inf'):
    print(-1)
else:
    print(answer)
        
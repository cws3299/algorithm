import sys
sys.stdin = open('22865.txt','r')
import heapq

def dijkstra1():
    global n,a,b,c,roads,m

    answer = [float('inf')]*(n+1)
    answer[a] = 0
    pq = []
    heapq.heappush(pq,[answer[a],a])

    while pq:
        now_distance , now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt ,wt in roads[now_position].items():
            distance = now_distance+wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return answer


def dijkstra2():
    global n,a,b,c,roads,m

    answer = [float('inf')]*(n+1)
    answer[b] = 0
    pq = []
    heapq.heappush(pq,[answer[b],b])

    while pq:
        now_distance , now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt ,wt in roads[now_position].items():
            distance = now_distance+wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return answer

def dijkstra3():
    global n,a,b,c,roads,m

    answer = [float('inf')]*(n+1)
    answer[c] = 0
    pq = []
    heapq.heappush(pq,[answer[c],c])

    while pq:
        now_distance , now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt ,wt in roads[now_position].items():
            distance = now_distance+wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return answer

def dijkstra():
    global n,a,b,c,roads,m

    answer = [float('inf')]*(n+1)
    visit = [0]*(n+1)
    answer[a] = 0
    answer[b] = 0
    answer[c] = 0
    visit[a] = 1
    visit[b] = 1
    visit[c] = 1
    pq = []
    heapq.heappush(pq,[answer[a],a])
    heapq.heappush(pq,[answer[b],b])
    heapq.heappush(pq,[answer[c],c])
    _max = 0
    dis = 0

    while pq:
        now_distance , now_position = heapq.heappop(pq)
    
        if visit[now_position] == 0:
            visit[now_position] = 1
            if now_distance > dis:
                dis = now_distance
                _max = now_position

        if answer[now_position] < now_distance:
            continue

        for nxt ,wt in roads[now_position].items():
            distance = now_distance+wt
            # print('+',wt,distance,now_distance)
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[distance,nxt])
                # print('----',answer[nxt],nxt)

    return _max

n = int(input())
a,b,c = map(int, input().split())
roads = {node:{} for node in range(n+1)}
m = int(input())
for _ in range(m):
    x,y,w = map(int, input().split())
    value = roads.get(x)
    vv = value.get(y)
    if vv == None or w<vv:
        roads[x][y] = w
        roads[y][x] = w

distance = dijkstra()

print(distance)
import sys
sys.stdin = open('18223.txt','r')
import heapq 

def dijkstra():
    global n,m,p,roads,short

    answer = [float('inf')]*(n+1)
    answer[1] = 0
    pq = []
    heapq.heappush(pq,[answer[1],1])

    while pq:
        now_distance, now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt , wt in roads[now_position].items():
            distance = now_distance + wt

            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    answer = answer[1:]
    short = answer[n-1]

    return

def dijkstra_go1(start,end):
    global n,m,p,roads,short,save

    answer = [float('inf')]*(n+1)
    answer[start] = 0
    pq = []
    heapq.heappush(pq,[answer[start],start])

    while pq:
        now_distance, now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt , wt in roads[now_position].items():
            distance = now_distance + wt

            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    save += answer[p]

    return


def dijkstra_go2(start,end):
    global n,m,p,roads,short,save

    answer = [float('inf')]*(n+1)
    answer[start] = 0
    pq = []
    heapq.heappush(pq,[answer[start],start])

    while pq:
        now_distance, now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt , wt in roads[now_position].items():
            distance = now_distance + wt

            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    save += answer[n]

    return


n,m,p= map(int, input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(m):
    s,e,w = map(int,input().split())
    value = roads.get(s)
    vv = value.get(e)
    if vv == None or vv > w:
        roads[s][e] = w
        roads[e][s] = w

short = 0

dijkstra()

save = 0
dijkstra_go1(1,p)


dijkstra_go2(p,n)


if short < save:
    print("GOOD BYE")
else:
    print("SAVE HIM")

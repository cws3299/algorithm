import sys
sys.stdin = open('17270.txt')
import heapq

def dijkstra1():
    global n,m,roads,start,answer

    pq = []
    answer[start] = 0
    heapq.heappush(pq,[answer[start],start])

    while pq:
        distance , position = heapq.heappop(pq)

        if answer[position] < distance:
            continue

        for nxt , wt in roads[position].items():
            new_distance = distance+wt
            if answer[nxt] > new_distance:
                answer[nxt] = new_distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return

def dijkstra2():
    global n,m,roads,end,bnawer

    pq = []
    bnawer[end] = 0
    heapq.heappush(pq,[bnawer[end],end])

    while pq:
        distance , position = heapq.heappop(pq)

        if bnawer[position] < distance:
            continue

        for nxt , wt in roads[position].items():
            new_distance = distance+wt
            if bnawer[nxt] > new_distance:
                bnawer[nxt] = new_distance
                heapq.heappush(pq,[bnawer[nxt],nxt])

    return
                

n,m = map(int, input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(m):
    a,b,w = map(int, input().split())
    value = roads.get(a)
    vv = value.get(b)
    if vv == None or w<vv:
        roads[a][b] = w
        roads[b][a] = w

start , end = map(int, input().split())

answer = [float('inf')]*(n+1)
bnawer = [float('inf')]*(n+1) 

dijkstra1()
dijkstra2()


cnswer = []
cns = float('inf')
for a in range(1,n+1):
    if answer[a] + bnawer[a]<cns and a != start and a != end:
        cns = answer[a] + bnawer[a]
        cnswer = []
        cnswer.append([a , answer[a] , bnawer[a]])
    elif answer[a] + bnawer[a]==cns and a != start and a != end:
        cnswer.append([a , answer[a] , bnawer[a]])

dnswer = []

for c in cnswer:
    if c[1] <= c[2]:
        dnswer.append([c[1]+c[2],c[0],c[1],c[2]])

dnswer.sort(key=lambda x:(x[0],x[2]))
# print(cnswer)
if dnswer == []:
    print(-1)
else:
    ans = dnswer[0][1]
    if ans == start or ans == end:
        print(-1)
    else:
        print(ans)
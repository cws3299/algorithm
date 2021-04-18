import sys
sys.stdin = open('2219.txt','r')
import heapq

def dijkstra():
    global n,m,roads,lst

    answer = [float('inf')]*(n+1)
    answer[1] = 0
    pq = []
    heapq.heappush(pq,[0,1,-1])
    
    while pq:
        now_distacne , now_position , pre_position = heapq.heappop(pq)

        if answer[now_position] < now_distacne:
            continue
        if pre_position != -1:
            lst.append([pre_position,now_position])

        for nxt,wt in roads[now_position].items():
            distance = now_distacne + wt

            if answer[nxt] > distance:
                # lst.append([now_position,nxt])
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt], nxt , now_position])

    return


n,m = map(int, input().split())
roads = {node:{} for node in range(n+1)}
lst = []

for _ in range(m):
    x,y,w = map(int, input().split())
    value = roads.get(x)
    vv = value.get(y)
    if vv == None or vv > w:
        roads[x][y] = w
        roads[y][x] = w

dijkstra()

print(len(lst))
for l in lst:
    print(l[0], end = ' ' )
    print(l[1])
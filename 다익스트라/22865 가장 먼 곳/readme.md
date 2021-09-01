[ 백준 : 가장 먼 곳 ] (https://www.acmicpc.net/problem/22865)



- 시간초과때문에 애먹은 문제

- 처음에는 a,b,c 세 곳에서 각각 다익스트라를 돌린 후 각자 나온 값들을 추가적으로 비교하는 과정으로 답을 구했다. 연산이 많아서 그런지 자연스레 시간초과

- 이후에 생각해낸 해결책은 하나의 다익스트라에  a,b,c의 위치를 한 번에 넣어주면서 거리가 가장 멀게 저장된 값을 갱신해주는 과정을 거쳤다.

  

```python
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
```


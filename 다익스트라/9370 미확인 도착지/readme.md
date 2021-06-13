[백준 : 미확인 도착지] (https://www.acmicpc.net/problem/9370)



- 다익스트라 문제
- 이렇게 까지 문제를 내야 하나 싶은 문제이다.
- 모든 도착 예상지가 간선으로 연결 안되어있을 수도 있다는 점을 명심하자!!!



```python
import sys
sys.stdin = open('9370.txt','r')
import heapq

def dijkstra_1():
    global n,m,c,s,g,h,roads,candidate,first

    answer = [float('inf')]*(n+1)
    pq = []
    answer[s] = 0
    heapq.heappush(pq,[answer[s],s])

    while pq:
        distance , position = heapq.heappop(pq)

        if position == g:
            first = g
            break

        if position == h:
            first = h
            break

        if answer[position] < distance:
            continue

        for nxt, wt in roads[position].items():
            new_distance = distance + wt
            if answer[nxt] > new_distance:
                answer[nxt] = new_distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return

def dijkstra_all():
    global n,m,c,s,g,h,roads,candidate,first

    answer = [float('inf')]*(n+1)
    pq = []
    answer[s] = 0
    heapq.heappush(pq,[answer[s],s])

    while pq:
        distance , position = heapq.heappop(pq)

        if answer[position] < distance:
            continue

        for nxt, wt in roads[position].items():
            new_distance = distance + wt
            if answer[nxt] > new_distance:
                answer[nxt] = new_distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return answer

def dijkstra_last():
    global n,m,c,s,g,h,roads,candidate,first,last

    answer = [float('inf')]*(n+1)
    pq = []
    answer[s] = 0
    heapq.heappush(pq,[answer[s],s])

    while pq:
        distance , position = heapq.heappop(pq)

        if position == first:
            break

        if answer[position] < distance:
            continue

        for nxt, wt in roads[position].items():
            new_distance = distance + wt
            if answer[nxt] > new_distance:
                answer[nxt] = new_distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return answer[first]

def dijkstra_last_go():
    global n,m,c,s,g,h,roads,candidate,first,last

    answer = [float('inf')]*(n+1)
    pq = []
    answer[last] = 0
    heapq.heappush(pq,[answer[last],last])

    while pq:
        distance , position = heapq.heappop(pq)

        if answer[position] < distance:
            continue

        for nxt, wt in roads[position].items():
            new_distance = distance + wt
            if answer[nxt] > new_distance:
                answer[nxt] = new_distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return answer

t = int(input())
for tc in range(t):
    n,m,c = map(int, input().split()) # 교차로 , 도로 , 목적지 후보
    s,g,h = map(int, input().split()) # 시작점 , 두 교차로

    first = None
    roads = {road:{} for road in range(n+1)}

    for _ in range(m):
        a,b,w = map(int, input().split())
        roads[a][b] = w
        roads[b][a] = w

    candidate = []
    for _ in range(c):
        ca = int(input())
        candidate.append(ca)

    dijkstra_1()
    
    last = None
    if first == g:
        last = h
    elif first == h:
        last = g


    # print('first',first)
    # print('last',last)

    answer1 = dijkstra_all()
    answer2 = dijkstra_last()
    answer3 = dijkstra_last_go()

    # print(answer1)
    # print(answer2)
    # print('---',roads[first][last])
    # print(answer3)

    for k in range(len(answer3)):
        answer3[k] += answer2
        answer3[k] += roads[first][last]

    answer = []
    for k in candidate:
        if answer1[k] == answer3[k] and answer1[k] != float('inf'):
            answer.append(k)

    answer.sort()

    for ans in answer:
        print(ans, end=' ')
    
    print()
```

![readme](readme.png)
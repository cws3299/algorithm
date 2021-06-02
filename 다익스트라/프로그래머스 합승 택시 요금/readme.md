[프로그래머스 : 카카오 2021 블라인드 / 합승택시 요금] (https://programmers.co.kr/learn/courses/30/lessons/72413)



- 예전에 못풀었어서 오랜만에 다시 도전했는데 의외로 쉽게 풀린 문제
- 원래는 한번의 다익스트라로 모든 문제를 해결하려고 했는데 이를 포기하고 a,b,s 각 지점 모두에서 다익스트라를 돌리고 세 지점을 통해 나온 answer값들을 더했을 때 가장 작은 위치의 값을 출력해준다. 해당 지점을 기점으로 각 방향으로 나뉜다





```python
import heapq

def dijkstra_a(n,s,a,b,roads):
    answer = [float('inf')]*(n+1)
    pq = []
    answer[a] = 0
    heapq.heappush(pq,[answer[a],a])

    
    while pq:
        now_distance, now_position = heapq.heappop(pq)
        
        if answer[now_position] < now_distance:
            continue
            
        for nxt,wt in roads[now_position].items():
            distance = now_distance + wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])      
    return answer

def dijkstra_b(n,s,a,b,roads):
    answer = [float('inf')]*(n+1)
    pq = []
    answer[b] = 0
    heapq.heappush(pq,[answer[b],b])

    
    while pq:
        now_distance, now_position = heapq.heappop(pq)
        
        if answer[now_position] < now_distance:
            continue
            
        for nxt,wt in roads[now_position].items():
            distance = now_distance + wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])      
    return answer

def dijkstra_s(n,s,a,b,roads):
    answer = [float('inf')]*(n+1)
    pq = []
    answer[s] = 0
    heapq.heappush(pq,[answer[s],s])

    
    while pq:
        now_distance, now_position = heapq.heappop(pq)
        
        if answer[now_position] < now_distance:
            continue
            
        for nxt,wt in roads[now_position].items():
            distance = now_distance + wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])      
    return answer

def solution(n, s, a, b, fares):
    answer = 0
    roads = {node:{} for node in range(n+1)}
    
    for fare in fares:
        roads[fare[0]][fare[1]] = fare[2]
        roads[fare[1]][fare[0]] = fare[2]
        
    aa = dijkstra_a(n,s,a,b,roads)
    bb = dijkstra_b(n,s,a,b,roads)
    ss = dijkstra_s(n,s,a,b,roads)
    ans = [0]*(n+1)
    for k in range(n+1):
        ans[k] += aa[k]
        ans[k] += bb[k]
        ans[k] += ss[k]
        # if k == a or k == b or k == s:
        #     ans[k] += float('inf')
    answer = min(ans)
    return answer
```


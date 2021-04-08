[백준 : 면접보는 승범이네] (https://www.acmicpc.net/problem/17835)



##### 2021.04.08



- 쉬웠던 다익스트라 문제
- 로직
- 일반 다익스트라와 똑같다, 다만 차이점은 두가지가 존재한다.
- roads를 시작에서 도착이 아닌, 도착에서 시작으로 구성한다.
- 다익스트라 안에서 pq안에 넣어주는 시작점에 면접장을 넣어준다
- 결과적으로 각 위치에서 면접장으로 가는 거리가 출력된다.
- index와 최대거리 출력하면 끝



```python
import sys
sys.stdin = open('17835.txt','r')
import heapq

def dijkstra():
    global n,m,k,roads,companys

    answer = [float('inf')]*(n+1)
    pq = []
    for company in companys:
        # print('company',company)
        heapq.heappush(pq,[0,company])
        answer[company] = 0

    while pq:
        now_distance, now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt,wt in roads[now_position].items():
            distance = now_distance + wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[distance,nxt])
    
    return answer

n,m,k = map(int, input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(m):
    s,e,w = map(int, input().split())
    value = roads.get(e)
    vv = value.get(s)
    if vv == None or vv > w:
        roads[e][s] = w
# print(roads)

companys = list(map(int, input().split()))

ans = dijkstra()
ans = ans[1:]

_max = max(ans)
index = ans.index(_max)
print(index+1)
print(_max)

```



![20210408_115122](20210408_115122.png)
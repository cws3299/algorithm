[백준 : 보석 줍기] (https://www.acmicpc.net/problem/2001)



- 비트마스킹과 bfs를 함께 활용한 문제
- 1에 보석이 있는경우를 유의해야한다
- 방문 처리의 경우 /섬의위치/가진보석 을 활용했다.
- 1에서 출발해 1에 다시 도착한 모든 경우의 보석의 수를 set에 저장 후 가장 큰 값을 반환한다.
- 팁을 하나쓰자면 보석이 있는 도시에서 보석을 줍는 경우
  - 보석을 이미 주웠나 중복체크 시행
  - 중복 아닐 경우 보석을 챙긴다. 
  - 다이아의 개수를 하나 늘린다
  - 새로운 다이아개수가 다리의 중량을 안넘는지 체크
  - 다리를 넘어감과 동시에 visit함수 체크



```python
import sys
sys.stdin = open('2001.txt','r')
from collections import deque

def bfs(now,vis):
    global n,m,k,lands,roads,visit

    q = deque()
    q.append([now,vis,0])
    # visit[now][vis] = 1
    answer = set()

    while q:
        now , vis , dia = q.popleft()

        # print(now,bin(vis),dia)

        if now == 1:
            if lands[now] != 0:
                if not vis&(1<<now):
                    answer.add(dia+1)
                else:
                    answer.add(dia)
            else:
                answer.add(dia)

        if lands[now] != 0:
            for k in range(2):
                if k == 0:
                    if not vis&(1<<lands[now]):
                        new_vis = vis|(1<<lands[now])
                        new_dia = dia + 1
                        visit[now][new_vis] = 1
                        for nxt,wt in roads[now].items():
                            if new_dia <= wt:
                                if visit[nxt][new_vis] == 0:
                                    visit[nxt][new_vis] = 1
                                    q.append([nxt,new_vis,new_dia])
                else:
                    # visit[now][vis] = 1
                    for nxt,wt in roads[now].items():
                        if dia <= wt:
                            if visit[nxt][vis] == 0:
                                visit[nxt][vis] = 1
                                q.append([nxt,vis,dia])

        else:
            # visit[now][vis] = 1
            for nxt,wt in roads[now].items():
                if dia <= wt:
                    if visit[nxt][vis] == 0:
                        visit[nxt][vis] = 1
                        q.append([nxt,vis,dia])

    return answer
            







n,m,k = map(int,input().split())
lands = [0]*(n+1)
for s in range(1,k+1):
    j = int(input())
    lands[j] = s

roads = {i:{} for i in range(n+1)}

for _ in range(m):
    a,b,w = map(int, input().split())
    roads[a][b] = w
    roads[b][a] = w

visit = [[0]*(1<<k+1) for _ in range(n+1)]

ans = bfs(1,0)

print(max(ans))

```

![20210628_090951](20210628_090951.png)
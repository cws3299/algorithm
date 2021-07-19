import sys
sys.stdin = open('9470.txt','r')
from collections import deque


t = int(input())
for tc in range(1,t+1):
    k,n,e = map(int, input().split())
    indegree = [0]*(n+1)
    strahler = [[0,0] for _ in range(n+1)]
    roads = [[] for _ in range(n+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        indegree[b] += 1
        roads[a].append(b)

    q = deque()

    for start in range(1,n+1):
        if indegree[start] == 0:
            strahler[start][0] = 1
            strahler[start][1] = 1
            q.append(start)


    while q:
        now = q.popleft()
        
        for nxt in roads[now]:
            if strahler[nxt][0] < strahler[now][0]:
                strahler[nxt][0] = strahler[now][0]
                strahler[nxt][1] = 1


                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    if strahler[nxt][1] >= 2:
                        strahler[nxt][0] += 1
                    q.append(nxt)

            elif strahler[nxt][0] == strahler[now][0]:
                strahler[nxt][1] += 1

                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    if strahler[nxt][1] >= 2:
                        strahler[nxt][0] += 1
                    q.append(nxt)

            else:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    if strahler[nxt][1] >= 2:
                        strahler[nxt][0] += 1
                    q.append(nxt)

    print(k , end =' ')
    print(strahler[n][0])
        




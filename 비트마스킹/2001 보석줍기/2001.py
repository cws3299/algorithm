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

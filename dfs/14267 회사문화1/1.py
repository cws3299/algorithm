import sys
sys.stdin = open('14267.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy
from collections import deque

def bfs(who,how):
    global n,m,go_down,answer,visit

    q = deque()
    q.append([who,how])

    while q:
        who, how = q.popleft()

        for nxt in go_down[who]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                answer[nxt] += how
                q.append([nxt,how])


    return


def child(start,now):
    global go_down, final_down

    q = deque()
    q.append(now)

    while q:
        now = q.popleft()

        for nxt in go_down[]


n,m = map(int, input().split())
go_up = [-1] + list(map(int, input().split()))
# go_down = [-1]*(n+1)
go_down = [[] for _ in range(n+1)]
final_down = deepcopy(go_down)
visit = [0]*(n+1)
answer = [0]*(n+1)
for k in range(1,n+1):
    down = go_up[k]
    if down != -1:
        go_down[down].append(k)

print(go_down)
for k in range(1,n+1):
    child(k,k)
    


for _ in range(m):
    who , how = map(int, input().split())

    answer[who] += how
    visit[who] = 1
    bfs(who,how)
    visit = [0]*(n+1)

answer = answer[1:]

for ans in answer:
    print(ans, end= ' ')

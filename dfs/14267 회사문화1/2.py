import sys
sys.stdin = open('14267.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy
from collections import deque

def dfs(start,who,how):
    global n,m,go_down,answer,visit,final_down,lst


    for nxt in go_down[who]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            answer[nxt] += how
            lst.append(nxt)
            dfs(start,nxt,how)

    if start == who:
        # print('++++', start,who)
        while len(lst) != 0:
            # print(lst)
            for ls in lst:
                visit[ls] = 0
                final_down[lst[0]].add(ls)
            if len(lst) > 0 :
                lst.popleft()

        
        
    return


n,m = map(int, input().split())
go_up = [-1] + list(map(int, input().split()))
go_down = [[] for _ in range(n+1)]
final_down = [set() for _ in range(n+1)]
visit = [0]*(n+1)
answer = [0]*(n+1)
for k in range(1,n+1):
    down = go_up[k]
    if down != -1:
        go_down[down].append(k)

lst = deque()

for _ in range(m):
    who , how = map(int, input().split())

    if final_down[who] == set():
        answer[who] += how
        visit[who] = 1
        lst.append(who)
        dfs(who,who,how)
        visit[who] = 0
        lst = deque()
    else:
        for final in final_down[who]:
            answer[final] += how

# print(answer)
# print(go_down)
answer = answer[1:]

# print(final_down)

for ans in answer:
    print(ans, end= ' ')
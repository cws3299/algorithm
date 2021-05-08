import sys
sys.stdin = open('14942.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy

def dfs(now,p):
    global n,powers,trees,visit,_mins

    for nxt , wt in trees[now]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            if _mins[nxt] == float('inf'):
                _mins[nxt] = p+wt
            p += wt
            dfs(nxt,p)
            p -= wt
            visit[nxt] = 0


    return

def go(start,now,remain):
    global n,powers,trees,visit,_mins,end,pos

    if _mins[now] < end:
        end = deepcopy(_mins[now])
        pos = deepcopy(now)
    elif _mins[now] > end:
        return

    for nxt , wt in trees[now]:
        if visit[nxt] == 0:
            if remain - wt >=0:
                visit[nxt] = 1
                remain -= wt
                go(start,nxt,remain)
                remain += wt
                visit[nxt] = 0

    return



n = int(input())
powers = [0]*(n+1)
for k in range(1,n+1):
    power = int(input())
    powers[k] = power

trees = [[] for _ in range(n+1)]
visit = [0]*(n+1)
_mins = [float('inf')] * (n+1)
answers = [0]*(n+1)

for k in range(n-1):
    s,e,w = map(int, input().split())
    trees[s].append([e,w])
    trees[e].append([s,w])

visit[1] = 1
_mins[1] = 0
dfs(1,0)

# print(visit)
# print(trees)
# print(_mins)
visit = [0]*(n+1)

for k in range(1,n+1):
    end = float('inf')
    pos = 0
    go(k,k,powers[k])
    answers[k] = pos

# print(answers)
answers = answers[1:]

for ans in answers:
    print(ans)
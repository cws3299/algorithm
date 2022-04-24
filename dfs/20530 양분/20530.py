import sys
sys.stdin = open('20530.txt','r')
sys.setrecursionlimit(200001)

def cycleDfs(pre, now):
    global cycleNode, flag, cyclePoint, visit, plusFlag

    for nxt in edges[now]:
        if pre != nxt:
            if visit[nxt] == 0:
                if flag == False:
                    visit[nxt] = 1
                    cycleDfs(now,nxt)
                    visit[nxt] = 0
                    if nxt == cyclePoint:
                        plusFlag = True

                    if plusFlag == False and flag == True:
                        cycleNode.append(nxt)
            else:
                cyclePoint = nxt
                cycleNode.append(nxt)
                flag = True
                return

    return

def settingUnionDfs(default, now):

    for nxt in edges[now]:
        if cycleVisit[nxt] == 0:
            if visit[nxt] == 0:
                visit[nxt] = 1
                parents[nxt] = default
                settingUnionDfs(default, nxt)

    return

n,q = map(int,input().split())
edges = [[] for _ in range(n+1)]
parents = [i for i in range(n+1)]

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

cycleNode = []
flag = False
plusFlag = False
cyclePoint = None
visit = [0] * (n+1)
cycleVisit = [0] * (n+1)
visit[1] = 1
cycleDfs(-1,1)

for k in cycleNode:
    cycleVisit[k] = 1

visit = [0] * (n+1)
for k in cycleNode:
    visit[k] = 1
    settingUnionDfs(k, k)

for _ in range(q):
    a,b = map(int, sys.stdin.readline().split())
    if parents[a] != parents[b]:
        print(2)
    else:
        print(1)
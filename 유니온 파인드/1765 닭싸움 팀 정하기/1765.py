import sys
sys.stdin = open('1765.txt','r')
from copy import deepcopy

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA <= rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB

    return

def find2(x):
    if final[x] == x:
        return x
    final[x] = find(final[x])
    return final[x]

def union2(a,b):
    rootA = find2(a)
    rootB = find2(b)

    if rootA <= rootB:
        final[rootB] = rootA
    else:
        final[rootA] = rootB

    return
  
def search(k,origin):
    global n,m,parents,final,visit

    pre = parents[k]
    if parents[k] != parents[pre]:
        union2(k,pre)
    else:
        if visit[pre] == 0:
            visit[pre] = 1
            final[pre] = origin
            search(pre,origin)

    return

n = int(input())
m = int(input())
parents = [i for i in range(n+1)]
parents2 = [i for i in range(n+1)]
visit = [0]*(n+1)
enemys = [[] for _ in range(n+1)]

for _ in range(m):
    w,a,b = map(str, input().split())
    a = int(a)
    b = int(b)
    if w == 'F':
        union(a,b)
    else:
        enemys[a].append(b)
        enemys[b].append(a)

for enemy in enemys:
    for e in enemy:
        for e2 in enemy:
            if find(e) != find(e2):
                union(find(e),find(e2))

final = deepcopy(parents)
# print(parents)
for k in range(n,0,-1):
    if visit[k] == 0:
        visit[k] = 1
        search(k,parents[k])

# print(final)
final = final[1:]
final = set(final)
print(len(final))

# print(parents)


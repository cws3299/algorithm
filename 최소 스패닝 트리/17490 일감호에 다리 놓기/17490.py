import sys
sys.stdin = open('17490.txt','r')
import heapq
from collections import deque

def mst1(node):
    global n,m,k,arr,roads,bridges,key,mstt,cnt,result

    q = deque()
    q.append(node)
    mstt[node] = 1
    cnt += 1

    while q:
        node = q.popleft()
        
        for nxt in roads[node]:
            if mstt[nxt] == 0:
                mstt[nxt] = 1
                q.append(nxt)
                cnt += 1

    return

def mst():
    global n,m,k,arr,roads,bridges,key,mstt,cnt,result

    
    # pq = []
    # key[n] = 0
    # heapq.heappush(pq,[key[n],n])
    
    for w, node in bridges:
        if mstt[node] == 0:
            result += w
            mst1(node)


    return

def pre_mst():
    global flag,n,m,k,arr,roads,bridges,key,mstt,cnt,result

    q = deque()
    q.append(0)
    cont = 1
    visit = [0]*n
    visit[0] = 1

    while q:
        node = q.popleft()

        for nxt in roads[node]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
                cont += 1

    if cont == n:
        flag = False
    else:
        flag = True

    return 

n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

key = [float('inf')] * (n+1)
mstt = [0] * (n+1)
cnt = 0
result =0

roads = [[] for _ in range(n)]
bridges = []

for idx, val in enumerate(arr):
    bridges.append([val,idx])

bridges.sort(key=lambda bridges:(bridges[0]))

for s in range(n):
    if s == 0:
        roads[s].append(s+1)
        roads[s].append(n-1)
    elif s == n-1:
        roads[s].append(s-1)
        roads[s].append(0)
    else:
        roads[s].append(s-1)
        roads[s].append(s+1)


for s in range(m):
    a,b = map(int, input().split())
    roads[a-1].remove(b-1)
    roads[b-1].remove(a-1)

# print(roads)

flag = False
pre_mst()
if flag == True:
    mst()

    # print(result)
    # print(roads)

    if cnt == n:
        if result <= k:
            print("YES")
        else:
            print("NO")
else:
    print("YES")
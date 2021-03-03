import sys
sys.stdin = open('14615.txt','r')
from collections import deque

def go1():
    global n,m,roads,roads2,visit,goo1,goo2

    q = deque()
    q.append(1)
    visit[1] = 1
    goo1[1] = 1

    while q:
        position = q.popleft()

        goo1[position] = 1

        for nxt in roads[position].keys():
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)

    return

def go2():
    global n,m,roads,roads2,visit,goo1,goo2

    q = deque()
    q.append(n)
    visit[n] = 1
    goo2[n] = 1

    while q:
        position = q.popleft()

        goo2[position] = 1

        for nxt in roads2[position].keys():
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)

    return


n,m = map(int, input().split())
roads = {node:{} for node in range(n+1)}
roads2 = {node:{} for node in range(n+1)}

for _ in range(m):
    s,e = map(int ,sys.stdin.readline().split())
    roads[s][e] = 1
    roads2[e][s] = 1

visit = [0]*(n+1)

goo1 = [0]*(n+1)
goo2 = [0]*(n+1)

go1()
visit = [0]*(n+1)
go2()

o = int(input())
for _ in range(o):
    p = int(sys.stdin.readline())
    if goo1[p] == 1 and goo2[p] == 1:
        print("Defend the CTP")
    else:
        print("Destroyed the CTP")
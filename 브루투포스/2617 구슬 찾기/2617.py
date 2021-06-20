import sys
sys.stdin = open('2617.txt','r')
from collections import deque

def big(g):
    global bigger, smaller, visit,bigg,smalll

    q = deque()
    visit[g] = 1
    # bigg += 1
    q.append(g)

    while q:
        now = q.popleft()

        for nxt in bigger[now]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
                bigg += 1

    return

def small(g):
    global bigger, smaller, visit,bigg,smalll

    q = deque()
    visit[g] = 1
    # smalll += 1
    q.append(g)

    while q:
        now = q.popleft()

        for nxt in smaller[now]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
                smalll += 1

    return



n,m = map(int, input().split())
bigger = [[] for _ in range(n+1)]
smaller = [[] for _ in range(n+1)]
mid = n//2

for _ in range(m):
    b,s = map(int, input().split())
    bigger[s].append(b)
    smaller[b].append(s)

answer = []
# print(bigger)
# print(smaller)

for g in range(1,n+1):
    bigg = 0
    smalll = 0
    visit = [0]*(n+1)
    big(g)
    small(g)
    # print(bigg,smalll,mid)
    if bigg <= mid and smalll<=mid:
        answer.append(g)
        

print(n-len(answer))


# 8:22
import sys
sys.stdin = open('1325.txt','r')
from collections import deque

def bfs(k):
    global n,m,arr,answer,compare

    q = deque()
    q.append(k)
    visit = [0]*(n+1)
    visit[k] = 1
    ans = 1

    while q:
        now = q.popleft()

        for nxt in arr[now]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                ans += 1
                q.append(nxt)

    return ans


n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[b].append(a)

answer = []
compare = 0

for k in range(1,n+1):
    if len(arr[k]) > 0:
        result = bfs(k)
        if result > compare:
            answer = []
            answer.append(k)
            compare = result
        elif result == compare:
            answer.append(k)
        
answer.sort()
for ans in answer:
    print(ans , end = ' ')
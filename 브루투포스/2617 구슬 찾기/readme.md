[백준 : 구슬 찾기] (https://www.acmicpc.net/problem/2617)



- 자신보다 큰 구슬을 저장하는 bigger배열과 자신보다 작은 구글을 저장하는 smaller배열을 만든다.
- 이후 자신보다 큰게 몇개인지 알기위해 bfs돌리고 작은게 몇개인지도 알기위해 bfs돌린다.
- 자기보다 큰것과 작은게 모두 전체//2 보다 작거나 같으면 가운데에 가능한 개수이다.
- 전체에서 가운데에 가능한 개수를 빼주면 가운데에 불가능한 개수인 정답을 구할 수 있다.



```python
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


```

![20210621_070430](20210621_070430.png)
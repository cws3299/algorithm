[백준 : 가장 가까운 공통 조상] (https://www.acmicpc.net/problem/3584)



##### 2021.04.23



- 로직
- 마지막에 주어지는 두개의 정점을 start,end라고 가정
- start의 자신을 포함한 모든 부모요소를 answers에 1로 마킹한다.
- end가 똑같이 dfs를 돌면서 answers가 1인애를 만나면 그게 바로 최초 공통 조상



```python
import sys
sys.stdin = open('3584.txt','r')
sys.setrecursionlimit(10**5)

def dfs(now):
    global n,start_parent,child,parent,answers

    if parent[start] == 0:
        return

    nxt = parent[now]

    if visit[nxt] == 0 and nxt != -1:
        visit[nxt] = 1
        answers[nxt] = 1
        dfs(nxt)

    return

def dfs1(now):
    global n,start_parent,child,parent,answers,answer

    # print(now)

    if answers[now] == 1:
        answer = now
        return

    nxt = parent[now]
    # print(now,nxt)
    if visit[nxt] == 0:
        visit[nxt] = 1
        dfs1(nxt)

    return
    
t = int(input())
for tc in range(t):
    n = int(input())
    parent = [0]*(n+1)
    child = [0]*(n+1)
    visit = [0]*(n+1)
    answers = [0]*(n+1)

    parent[0] = -1
    child[0] = -1

    for _ in range(n-1):
        a,b = map(int, input().split())
        parent[b] = a
        child[a] = b

    start , end = map(int, input().split())


    start_parent = []

    answer = 0

    answers[start] = 1
    dfs(start)
    visit = [0]*(n+1)
    dfs1(end)

    # print(parent)
    # print(child)
    # print(answers)
    print(answer)
```

![readme](readme.png)
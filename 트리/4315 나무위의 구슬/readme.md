[ 백준 : 나무 위의 구슬 ] (https://www.acmicpc.net/problem/4315)



- 2021년 7월 26일에 푼 문항

- 프로그래머스의 `0으로 만들기` 문제와 유사한 방식으로 해결했다.
- 다만 초기에 여러번 틀렸던 이유는 dfs의 시작점을 root로 하지 않았었기  때문
- root노드를 찾은 후 dfs에 root노드를 넣어주면서 탐색을 시작했다.



```python
import sys
sys.stdin = open('4315.txt','r')
sys.setrecursionlimit(300000)

def dfs(x):
    global n,marbles,roads,visit,answer

    now = marbles[x]
    visit[x] = 1

    for nxt in roads[x]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            now += dfs(nxt)

    answer += abs(now)

    return now

while True:
    n = int(input())
    if n != 0:
        marbles = [0]*(n+1)
        roads = [[] for _ in range(n+1) ]
        visit = [0]*(n+1)
        answer = 0
        parents = [0]*(n+1)
        for _ in range(n):
            arr = list(map(int, input().split()))
            if len(arr) == 3:
                a = arr[0]
                b = arr[1]
                marbles[a] = b-1
            else:
                a = arr[0]
                b = arr[1]
                nxt = arr[3:]
                marbles[a] = b-1
                roads[a] = nxt
                for nx in nxt:
                    parents[nx] = 1
        parents[0] = 1
        root = parents.index(0)
        dfs(root)

        print(answer)
    else:
        break
```

![20210726_001258](20210726_001258.png)
[백준 1613  : 역사] (https://www.acmicpc.net/problem/1613)



#### 플로이드 와샬 알고리즘을 공부한 후 풀어본 활용 문제!!!



- 1과 -1 ,0 을 활용하는 것만 이해하면 기존 플로이드 와샬과 큰 차이가 없는 문제



2021.03.09



```python
import sys
sys.stdin = open('1613.txt','r')
from copy import deepcopy

def floyid():
    global n,m,arr

    dist = [[float('inf')]*(n+1) for _ in range(n+1)]

    for y in range(1,n+1):
        for x in range(1,n+1):
            dist[y][x] = arr[y][x]

    for k in range(1,n+1):
        for st in range(1,n+1):
            for en in range(1,n+1):
                if dist[st][k] == -1 and dist[k][en] == -1: # st k en 순서일 경우
                    dist[st][en] = -1
                    dist[en][st] = 1
                elif dist[st][k] == -1 and dist[k][en] == 1:
                    pass
                elif dist[st][k] == 1 and dist[k][en] == -1:
                    pass
                elif dist[st][k] == 1 and dist[k][en] == 1: # en k st 순서일 경우
                    dist[en][st] = -1
                    dist[st][en] = 1

    arr = deepcopy(dist)
    return
            

n,m = map(int, input().split())
arr = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    f,e = map(int, input().split())
    arr[f][e] = -1
    arr[e][f] = 1

for y in range(n+1):
    for x in range(n+1):
        if y == x:
            arr[y][x] = 0

floyid()

# for ar in arr[1:]:
#     for a in ar[1:]:
#         if a == float('inf'):
#             a = 0
#         print(a, end = ' ')
#     print()

c = int(input())
for _ in range(c):
    s,e = map(int,input().split())
    if arr[s][e] == float('inf'):
        arr[s][e] = 0
    print(arr[s][e])
```



![20210309_144432](20210309_144432.png)
[백준 11404 : 플로이드] (https://www.acmicpc.net/problem/11404)



#### 플로이드 와샬 알고리즘에 대한 공부를 한 후 처음 풀어본 플로이드 와샬 문제



- 기본적인 플로이드 와샬 알고리즘 구현 문제이다.
- 플로이드 와샬 알고리즘 이란?
  - 다익스트라 알고리즘은 한 정점에서 다른 모든 정점을 향하는 최소경로를 뽑아낸다면 플로이드 와샬 알고리즘은 각 정점에서 다른 모든 정점에 대한 최단경로가 표현된다. 그렇기 때문에 플로이드 와샬은 초기 세팅 배열이 2차원이다.

2021.03.09



```python
import sys
sys.stdin = open('11404.txt','r')
from copy import deepcopy

# 플로이드 와샬 알고리즘
def floyd():
    global arr,n,m

    dist = [[float('inf')]*(n+1) for _ in range(n+1)]

    # print(arr)
    # print(dist)
    for y in range(1,n+1):
        for x in range(1,n+1):
            dist[y][x] = arr[y][x]

    # print(dist)
    
    # 기본적인 알고리즘 -> 시작점과 끝점 , 그리고 중간지점 세가지의 지점을 활용해서 문제를 푼다.
    
    # 쉬운예시를 들면
    # 1,2,3 세가지 지점이 존재한다.
    # 1 -> 3의 지점의 거리가 8이다. 그런데 2를 거쳐간다면 1->2 (2) 2->3 (4)일 경우 6을 통해서만으로도 1에서 3을 향해 갈 수 있다. 이러한 과정으로 최솟값을 지속적으로 갱신해준다. 


    for k in range(1,n+1):
        for st in range(1,n+1):
            for en in range(1,n+1):
                if dist[st][en] > dist[st][k] + dist[k][en]: # 갱신이 되는 조건은 연결되지 않았던 정점간의 거리가 연결된다는 것을 의미 하거나 더 짧은 경로로 갱신됨을 의미한다.
                    dist[st][en] = dist[st][k] + dist[k][en]

    arr = deepcopy(dist)

    return



n = int(input())
m = int(input())

# 초기 세팅
arr = [[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int, input().split())
    if arr[a][b] > w and a != b:
        arr[a][b] = w

for y in range(1,n+1):
    for x in range(1,n+1):
        if y == x:
            arr[y][x] = 0

floyd()

# 출력
for ar in arr[1:]:
    for a in ar[1:]:
        if a == float('inf'):
            a = 0
        print(a , end = ' ')
    print()
    
 
```





###### 코드는 생각보다 간단하지만 짧은 코드내에서 생각할 거리가 굉장히 많은 알고리즘인 것 같다. 은근히 헷갈림.......
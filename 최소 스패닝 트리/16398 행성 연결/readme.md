[백준 - 행성 연결] (https://www.acmicpc.net/problem/16398)



정말 간단한 mst 문제

- mst 문제를 오랜만에 풀다보니 다익스트라랑 뇌가 짬뽕되서 5분 좀 넘게 해맨것 같다.



```python
import sys
sys.stdin = open('16398.txt','r')
import heapq

# 2021.03.03

def mst():
    global n,roads

    answer = [float('inf')]*(n+1)
    mst = [0]*(n+1)
    pq= []
    result = 0
    answer[1] = 0
    heapq.heappush(pq,[answer[1],1])

    while pq:
        now_distance , now_position = heapq.heappop(pq)

        # print(now_distance,now_position)

        if mst[now_position] != 0:
            continue

        result += now_distance
        mst[now_position] = 1

        for nxt,wt in roads[now_position].items():

            if mst[nxt] == 0 and answer[nxt] > wt:
                answer[nxt] = wt
                heapq.heappush(pq,[answer[nxt],nxt])

    # print(answer)
    # print(result)
    return result

n = int(input())
roads = {node:{} for node in range(n+1)}

for s in range(n):
    arr1 = list(map(int, input().split()))
    for e in range(n):
        w = arr1[e]
        roads[s+1][e+1] = w
        roads[e+1][s+1] = w

print(mst())

# print(roads)
```



![20210303_155153](20210303_155153.png)



코드 효율화는 처음에 받을때 2차원 배열이라 ij랑 ji가 같기 때문에 받는것 수정해주면 속도가 조금더 오를 것 같다.
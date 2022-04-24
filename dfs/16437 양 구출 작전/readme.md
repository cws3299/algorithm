양 구출 작전 (https://www.acmicpc.net/problem/16437)



- 골드2

- dfs로 전체를 돌면 되는 문제이다.
- 예전에는 못 풀었는데, 다시 풀어보니 너무 쉬워서 당황스러웠다.
- 싸이클이 없기 때문에, 방문처리를 안해줘도 된다.



```python
import sys
sys.setrecursionlimit(123459)
sys.stdin = open('16437.txt', 'r')

def dfs(nowNode):
    global answer, visitCnt

    visitCnt += 1

    if len(edges[nowNode]) == 0:
        if animalKinds[nowNode] == 'S':
            value[nowNode] = animalCnt[nowNode]
            return animalCnt[nowNode]
        else:
            value[nowNode] = 0
            return 0

    if animalKinds[nowNode] == 'S':
        value[nowNode] += animalCnt[nowNode]
    else:
        value[nowNode] -= animalCnt[nowNode]

    for nxtNode in edges[nowNode]:
        value[nowNode] += dfs(nxtNode)

    if nowNode == 1 and visitCnt == n:
        answer = value[nowNode]

    if value[nowNode] < 0:
        return 0
    else:
        return value[nowNode]

n = int(sys.stdin.readline())
edges = {i:[] for i in range(1,n+1)}
animalKinds = [0] * (n+1)
animalCnt = [0] * (n+1)
value = [0] * (n+1)
for k in range(2,n+1):
    animal, cnt, connectNode = map(str, sys.stdin.readline().split())
    connectNode = int(connectNode)
    cnt = int(cnt)
    edges[connectNode].append(k)
    animalKinds[k] = animal
    animalCnt[k] = cnt

answer = 0
visitCnt = 0
dfs(1)

print(answer)
```


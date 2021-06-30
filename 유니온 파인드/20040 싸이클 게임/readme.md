[백준 : 싸이클 게임] (https://www.acmicpc.net/problem/20040)



- 코테 탈락해서 기분이 꿀꿀한 밤.....
- 문제를 풀어보았다
- 일반적인 분리집합 문제 그 자체다.



```python
import sys
sys.stdin = open('20040.txt','r')

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]
    

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return False

    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB
    
    return True

n,m = map(int, input().split())
parents = [i for i in range(n)]
answer = 0
for k in range(1,m+1):
    a,b = map(int, input().split())
    result = union(a,b)
    if result == False:
        answer = k
        break

print(answer)
```

![20210630_210939](20210630_210939.png)
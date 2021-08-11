[ 백준 : 친구비 ] (https://www.acmicpc.net/problem/16562)



- 2021-08-10에 푼 문제
- 생각보다 쉽게 풀렸다



```python
import sys
sys.stdin = open('16592.txt','r')
from collections import defaultdict
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA > rootB:
        parents[rootA] = rootB
    elif rootB > rootA:
        parents[rootB] = rootA

    return

n,m,money = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0,0)
dictt = defaultdict(int)
parents = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    union(a,b)
for p in range(n+1):
    pp = find(p)
    mo = arr[p]
    if dictt[pp] == 0 or mo<dictt[pp]:
        dictt[pp] = mo

parents = set(parents)
answer = 0
for p in parents:
    answer += dictt[p]

if answer <= money:
    print(answer)
else:
    print("Oh no")


```

![20210810_110438](20210810_110438.png)
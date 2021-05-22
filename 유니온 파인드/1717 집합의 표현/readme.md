[백준 : 집합의 표현] (https://www.acmicpc.net/problem/1717)



- 전형적인 분리집합의 기초를 닦는 문제
- 처음에는 살짝 헷갈렸지만 할만했다.



```python
import sys
sys.stdin = open('1717.txt','r')

def find(a):
    if arr[a] == a:
        return a
    arr[a] = find(arr[a])
    return arr[a]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        arr[rootB] = rootA
    return

def check(a,b):
    if find(a) == find(b):
        return True
    else:
        return False



n,m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    choice,a,b = map(int,input().split())
    if choice == 0:
        union(a,b)
    else:
        ans = check(a,b)
        if ans == True:
            print('YES')
        else:
            print('NO')

```

![20210522_150218](20210522_150218.png)
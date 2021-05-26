[백준 : 거짓말] (https://www.acmicpc.net/problem/1043)



- 일반적인 유니온  파인드 문제
- 일단 처음에 아는 사람이 0인경우를 예외처리 해준다.
- 처음부터 진실을 아는 사람이 있을 경우 그 사람들을 모두 union해준다. (가장 작은 숫자가 루트가 되도록 point)
- 그 다음 주어진 파티의 인원들도 모두 유니온 파인드 해준다.
- 각 파티의 인원들을 새로 담은 arr배열을 다시 돌려주면서 각 파티인원들 중 한 명이라도 부모가 point의 parents와 같으면 거짓말을 할 수 없는 파티의 수에 +1을 해준다.
- 마지막에
- 전체 파티 - 거짓말을 할 수 없는 파티를 빼주면 거짓말을 할 수 있는 파티가 나온다.



```python
import sys
sys.stdin = open('1043.txt','r')

def find(a):
    global n,m,parents

    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a,b):
    global n,m,parents

    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB

    return



n,m = map(int, input().split())
parents = [i for i in range(n+1)]

checks = list(map(int, input().split()))

if checks[0] > 0:
    c = checks[0]
    checks = checks[1:]

    checks.sort()

    point = checks[0]

    for c in range(1,len(checks)):
        union(point,checks[c])

    arr = []

    for _ in range(m):
        lst = list(map(int, input().split()))
        a = lst[0]
        lst = lst[1:]
        lst.sort()
        num = lst[0]
        for c in range(1,len(lst)):
            union(num,lst[c])
        arr.append(lst)

    no_lie = 0
    for ar in arr:
        for a in ar:
            if find(parents[a]) == find(parents[point]):
                no_lie += 1
                break

    print(m-no_lie)
else:
    print(m)
```

![20210526_124854](20210526_124854.png)
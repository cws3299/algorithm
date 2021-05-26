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

    # print(point)
    # print(parents)
    # print(arr)

    no_lie = 0
    for ar in arr:
        for a in ar:
            if find(parents[a]) == find(parents[point]):
                no_lie += 1
                break

    # print(no_lie)
    print(m-no_lie)
else:
    print(m)
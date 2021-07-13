import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('7511.txt','r')
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB

    return

def check(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootB == rootA:
        return True
    else:
        return False

t = int(input())
for tc in range(1,t+1):
    print('Scenario {}:'.format(tc))
    n = int(input())
    m = int(input())
    parents = [i for i in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        union(a,b)

    k = int(input())
    for _ in range(k):
        a,b = map(int, input().split())
        result = check(a,b)
        if result == True:
            print(1)
        else:
            print(0)
    print()

    # print(parents)
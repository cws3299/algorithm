import sys
sys.stdin = open('10775.txt','r')
sys.setrecursionlimit(10**5)

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    parents[rootB] = rootA

n = int(input())
m = int(input())

parents = [i for i in range(n+1)]
visit = [0] * (n+1)

flag = True
answer = 0

# 6에서 6 => 6
# 또 6에서 6 => 5
# 또 6에서 6 => 4

for _ in range(m):
    k = int(input())
    pk = find(k)
    if visit[pk] == 0:
        visit[pk] = 1
        if pk != 1:
            union(pk-1,k)
        else:
            union(pk,k)
    else:
        pk = pk-1
        if pk == 0:
            break
        visit[pk] = 1
        union(pk,k)

    answer += 1

print(answer)


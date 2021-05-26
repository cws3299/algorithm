import sys
sys.stdin = open('4195.txt','r')
from collections import defaultdict

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parents[rootB] = rootA
        total[rootA] += total[rootB]

    return


tc = int(input())
for _ in range(tc):
    n = int(input())
    dict_ = defaultdict(int)
    parents = [i for i in range(n+1)]
    total = [1]*(n+1)
    number = 0
    for _ in range(n):
        a,b = map(str, input().split())
        value = dict_.get(a)
        value2 = dict_.get(b)
        if value == None:
            dict_[a] = number
            number += 1
        if value2 == None:
            dict_[b] = number
            number += 1

        union(dict_[a],dict_[b])

        result = min(dict_[a],dict_[b])
        tmp = find(parents[result])
        print(total[tmp])


import sys
sys.stdin = open('18116.txt','r')

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)
    # print(rootA, rootB)

    if rootA < rootB:
        ss = find(rootA)
        sb = find(rootB)
        parents[rootB] = rootA
        numbers[ss] += numbers[sb]
        numbers[sb] = 0
        # print(ss,sb,numbers[ss],numbers[sb])
    elif rootA > rootB:
        ss = find(rootB)
        sb = find(rootA)
        parents[rootA] = rootB
        numbers[ss] += numbers[sb]
        numbers[sb] = 0

    return

n = int(input())
parents = [i for i in range(11)]
numbers = [1]*(11)
for _ in range(n):
    arr = list(map(str, sys.stdin.readline().split()))
    if len(arr) == 3:
        union(int(arr[1]),int(arr[2]))
        # print(numbers)
    else:
        ss = find(parents[int(arr[1])])
        print(numbers[ss])

# print(numbers)



import sys
sys.stdin = open('11404.txt','r')
from copy import deepcopy

def floyd():
    global arr,n,m

    dist = [[float('inf')]*(n+1) for _ in range(n+1)]

    # print(arr)
    # print(dist)
    for y in range(1,n+1):
        for x in range(1,n+1):
            dist[y][x] = arr[y][x]

    # print(dist)


    for k in range(1,n+1):
        for st in range(1,n+1):
            for en in range(1,n+1):
                if dist[st][en] > dist[st][k] + dist[k][en]:
                    dist[st][en] = dist[st][k] + dist[k][en]

    arr = deepcopy(dist)

    return



n = int(input())
m = int(input())

arr = [[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int, input().split())
    if arr[a][b] > w and a != b:
        arr[a][b] = w

for y in range(1,n+1):
    for x in range(1,n+1):
        if y == x:
            arr[y][x] = 0

floyd()

for ar in arr[1:]:
    for a in ar[1:]:
        if a == float('inf'):
            a = 0
        print(a , end = ' ')
    print()
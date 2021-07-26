import sys
sys.stdin = open('4315.txt','r')
sys.setrecursionlimit(300000)

def dfs(x):
    global n,marbles,roads,visit,answer

    now = marbles[x]
    visit[x] = 1

    for nxt in roads[x]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            now += dfs(nxt)

    answer += abs(now)

    return now

while True:
    n = int(input())
    if n != 0:
        marbles = [0]*(n+1)
        roads = [[] for _ in range(n+1) ]
        visit = [0]*(n+1)
        answer = 0
        parents = [0]*(n+1)
        for _ in range(n):
            arr = list(map(int, input().split()))
            if len(arr) == 3:
                a = arr[0]
                b = arr[1]
                marbles[a] = b-1
            else:
                a = arr[0]
                b = arr[1]
                nxt = arr[3:]
                marbles[a] = b-1
                roads[a] = nxt
                for nx in nxt:
                    parents[nx] = 1
        parents[0] = 1
        root = parents.index(0)
        dfs(root)

        print(answer)
    else:
        break
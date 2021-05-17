import sys
sys.stdin = open('12978.txt','r')
sys.setrecursionlimit(10**5)

def solve(num):
    visit[num] = 1
    dp[num][0] = 0
    dp[num][1] = 1

    for i in edges[num]:
        if visit[i] == 0:
            solve(i)
            dp[num][0] += dp[i][1]
            dp[num][1] += min(dp[i][0],dp[i][1])

    return

n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visit = [0]*(n+1)

dp = [[0,0] for _ in range(n+1)]

solve(1)
print(min(dp[1][0],dp[1][1]))
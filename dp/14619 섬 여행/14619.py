import sys
sys.stdin = open('14619.txt','r')
sys.setrecursionlimit(10**5)
import heapq

def go(l,b,ll,bb):
    global n,m,heights,bridges,dp

    if b == 0:
        # heapq.heappush(pq,[l])
        dp[ll][bb] = heights[l]
        return heights[l]

    if dp[l][b] != float('inf'):
        return dp[l][b]

    for nxt in bridges[l]:
        dp[l][b] = min(dp[l][b],go(nxt,b-1,ll,bb)) 

    return dp[l][b]

n,m = map(int, input().split())
heights = [0] + list(map(int, input().split()))
bridges = [[] for bridge in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    bridges[a].append(b)
    bridges[b].append(a) 

dp = [[float('inf')]*501 for _ in range(n+1)]

answer_lst = []
    

t = int(input())
for _ in range(t):
    a,k = map(int ,input().split())
    # pq = []
    go(a,k,a,k)
    if dp[a][k] == float('inf'):
        print(-1)
    else:
        print(dp[a][k])
    # print(dp[a][k])

# print(dp)


# print(bridges)

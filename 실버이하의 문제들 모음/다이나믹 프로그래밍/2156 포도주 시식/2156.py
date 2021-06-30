import sys
sys.stdin = open('2156.txt','r')
sys.setrecursionlimit(int(1e9))
N = int(input())
wines = [0] + [int(input()) for _ in range(N)]
# 바로 전칸하고 마신값, 전전칸마시고 마시거나 안마시거나
dp = [[-1, -1] for _ in range(N + 1)]
dp[0] = [0, 0]
def drink(idx):
    if idx == 1:
        dp[idx] = [wines[1], wines[1]]
        return
    if dp[idx - 1] == [-1, -1]:
        drink(idx - 1)
    if dp[idx - 2] == [-1, -1]:
        drink(idx - 2)
    dp[idx][0] = wines[idx] + dp[idx - 1][1]
    dp[idx][1] = max(wines[idx] + max(dp[idx - 2]), dp[idx - 1][0])


drink(N)
print(max(dp[N]))
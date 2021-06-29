import sys
sys.stdin = open('11057.txt','r')
sys.setrecursionlimit(10**5)

def go(pos,num):
    global n,dp

    if pos == n:
        dp[pos][num] = 1
        return dp[pos][num]
    
    if dp[pos][num] != 0:
        return dp[pos][num]

    for k in range(10):
        if k >= num:
            dp[pos][num] += go(pos+1,k)

    return dp[pos][num]


n = int(input())

dp = [[0]*10 for _ in range(n+1)]

go(0,0)

print(dp[0][0]%10007)
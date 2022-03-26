import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('1176.txt','r')

def makeDp(nowNode, visit):

    if visit == endPoint:
        return 1

    if dp[nowNode][visit] != 0:
        return dp[nowNode][visit]


    for nxtNode in range(1,n+1):
        if not visit & (1<<nxtNode):
            if nowNode == 0:
                dp[nowNode][visit] += makeDp(nxtNode, visit|(1<<nxtNode))
            else:
                if abs(heights[nowNode] - heights[nxtNode]) > k:
                    dp[nowNode][visit] += makeDp(nxtNode, visit|(1<<nxtNode))


    return dp[nowNode][visit]

n,k = map(int, input().split())
heights = []
heights.append(float('inf'))

for _ in range(n):
    tall = int(input())
    heights.append(tall)

dp = [[0] * (1<<n+1) for _ in range(n+1)]

endPoint = 0
for nxt in range(1,n+1):
    endPoint |= 1<<nxt

makeDp(0,0)

print(dp[0][0])
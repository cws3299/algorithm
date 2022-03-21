import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('1102.txt','r')

def makeDp(nowNode, visited):
    global dp

    cnt = 0
    for pos in range(n):
        if visited & (1<<pos):
            cnt += 1

    if cnt == targetCnt:
        return 0

    if dp[nowNode][visited] != INF:
        return dp[nowNode][visited]

    for nxtNode in range(n):
        if not visited & (1<<nxtNode):
            minNode = INF
            for goNode in range(n):
                if visited & (1<<goNode) and costs[goNode][nxtNode] < minNode:
                    minNode = costs[goNode][nxtNode]
            dp[nowNode][visited] = min(dp[nowNode][visited], makeDp(nxtNode, visited|1<<nxtNode) + minNode)

    return dp[nowNode][visited]

n = int(input())
costs = []
for _ in range(n):
    costRow = list(map(int, input().split()))
    costs.append(costRow)

state = list(input())

targetCnt = int(input())

visit = 0
firstCnt = 0

for t in range(len(state)):
    targetState = state[t]
    if targetState == 'Y':
        visit|=(1<<t)
        firstCnt += 1

INF = float('inf')
dp = [[INF] * (1<<n) for _ in range(n)]

if firstCnt >= targetCnt:
    print(0)
elif firstCnt == 0 and targetCnt > 0:
    print(-1)
else:    
    makeDp(t,visit)
    print(dp[t][visit])

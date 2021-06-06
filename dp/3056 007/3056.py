import sys
sys.stdin = open('3056.txt','r')
sys.setrecursionlimit(10**5)
from math import floor

def go(depth,visit,de,co):
    global n,arr,dp,answer,visited

    if depth == n:
        return 1
        
    if dp[visit] != -1:
        return dp[visit]

    dp[visit] = -100000

    for i in range(n):
        if not visit&(1<<i):
            de += 1
            co -= 1
            visited = visit|(1<<i)
            dp[visit] = max(dp[visit], go(depth+1,visited,de,co)*(arr[depth][i]/100))
            de -= 1
            co += 1

    # if dp[visit] > answer:
    #     answer = dp[visit]
    
    return dp[visit]

n = int(input())
arr = []
for _ in range(n):
    arr1 = list(map(int,input().split()))
    arr.append(arr1)

dp = [-1]*(1<<n)
visited = [0]*n

answer = 0


print("{:.6f}".format(go(0,0,1,n)*100))
# a = answer/(100**(n-1))
# print(dp)

# print("{:.6f}".format(answer*100))
# print(answer)
# print(answer/100**(n-1))
# print(dp)
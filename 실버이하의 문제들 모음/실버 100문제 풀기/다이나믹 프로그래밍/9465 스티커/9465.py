import sys
sys.stdin = open('9465.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for _ in range(2):
        ar = list(map(int, input().split()))
        arr.append(ar)

    dp = [[0]*n for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]+arr[1][0]
    dp[1][0] = arr[1][0]
    dp[1][1] = arr[1][1]+arr[0][0] 
    dp[0][2] = max(arr[0][0]+arr[1][1],arr[1][0])+arr[0][2]
    dp[1][2] = max(arr[1][0]+arr[0][1],arr[0][0])+arr[1][2]

    for x in range(3,n):
        for y in range(2):
            if y == 0:
                dp[y][x] = max(dp[y][x-2],dp[y+1][x-1],dp[y+1][x-2])+arr[y][x]
            else:
                dp[y][x] = max(dp[y][x-2],dp[y-1][x-1],dp[y-1][x-2])+arr[y][x]

    print(max(dp[0][n-2],dp[0][n-1],dp[1][n-2],dp[1][n-1]))

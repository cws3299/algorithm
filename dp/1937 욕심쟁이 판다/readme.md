[백준 : 욕심쟁이 판다] (https://www.acmicpc.net/problem/1937)



- 너비우선 탐색 + dp문제
- 예전에 풀었던 문제라 다시 풀어보았다.
- 쉽게는 풀었으나 재귀관련 오류를 겪었다



```python
import sys
sys.stdin = open('1937.txt','r')
sys.setrecursionlimit(10**5)

def go(y,x):
    global n,arr,dp

    if dp[y][x] != 0:
        return dp[y][x]

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<n:
            if arr[ny][nx] > arr[y][x]:
                dp[y][x] = max(go(ny,nx)+1, dp[y][x])

    return dp[y][x]


dy = [0,0,-1,1]
dx = [1,-1,0,0]
n = int(input())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

dp = [[0]*n for _ in range(n)]

for y in range(n):
    for x in range(n):
        go(y,x)

answer = 0
for y in range(n):
    for x in range(n):
        if dp[y][x] > answer:
            answer = dp[y][x]

# print(dp)
print(answer+1)
```

![20210525_201458](20210525_201458.png)
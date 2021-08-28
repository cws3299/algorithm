[ 백준 : 텔레포트3 ] (https://www.acmicpc.net/problem/12908)



- 백트래킹으로 푸는 문제같아보였다.
- 그런데 그냥 8개의 정점간 위치를 저장해놓고 8개의 지점을 중심으로만 dfs돌리면 값이 나올 것 같아서 백트래킹이 아닌 초기 설정 후 일반 dfs방식으로 해결했다.



```python
import sys
sys.stdin = open('12908.txt','r')
sys.setrecursionlimit(10**5)

def dfs(now,cnt):
    global move , answer , visit

    if now == 1:
        if cnt < answer:
            answer = cnt
        return

    for nxt in range(8):
        if visit[nxt] == 0:
            visit[nxt] = 1
            cnt += move[now][nxt]
            dfs(nxt,cnt)
            cnt -= move[now][nxt]
            visit[nxt] = 0

    return

positions = [0]*8

sy,sx = map(int,input().split())
ey,ex = map(int,input().split())

positions[0] = [sy,sx]
positions[1] = [ey,ex] 

tel = list(map(int,input().split()))
positions[2] = [tel[0],tel[1]]
positions[3] = [tel[2],tel[3]]

tel = list(map(int,input().split()))
positions[4] = [tel[0],tel[1]]
positions[5] = [tel[2],tel[3]]

tel = list(map(int,input().split()))
positions[6] = [tel[0],tel[1]]
positions[7] = [tel[2],tel[3]]

move = [[float('inf')]*8 for _ in range(8)]

for p1 in range(8):
    for p2 in range(8):
        a = abs(positions[p1][0] - positions[p2][0])
        b = abs(positions[p1][1] - positions[p2][1])
        if move[p1][p2] > a+b:
            move[p1][p2] = a+b
            move[p2][p1] = a+b

if move[2][3] > 10:
    move[2][3] = 10
    move[3][2] = 10

if move[4][5] > 10:
    move[4][5]  = 10
    move[5][4]  = 10

if move[6][7] > 10:
    move[6][7] = 10
    move[7][6] = 10

answer = float('inf')
visit = [0]*8
visit[0] = 1
dfs(0,0)

print(answer)
```

![20210824_173236](20210824_173236.png)
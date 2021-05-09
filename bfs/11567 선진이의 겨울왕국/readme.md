[백준 : 선진이의 겨울왕국] (https://www.acmicpc.net/problem/11567)



- 정말 단순한 bfs문제!! 왜 이렇게 정답률이 낮은지 이해하기 힘들다
- 시작점에서 이동한다. 도착점이 아닐경우 '.'인 경우 가고 'X'인 경우에는 가지 않는다.
- 도착점인 경우 깨진경우에 다시 도착하면 return False, 안 깨진 상태에서 처음 밟은거면 다시 q에 넣어준다.
- 최종적으로 False를 반환하면 성공 True를 반환하면 실패이다.



```python
import sys
sys.stdin = open('11567.txt','r')
from collections import deque

def bfs():
    global n,m,arr,sy,sx,ey,ex

    q = deque()
    q.append([sy,sx])

    while q:
        y,x = q.popleft()

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if not (ny == ey and  nx == ex):
                    if arr[ny][nx] == '.':
                        arr[ny][nx] = 'X'
                        q.append([ny,nx])
                else:
                    if arr[ny][nx] == '.':
                        arr[ny][nx] = 'X'
                        q.append([ny,nx])
                    else:
                        return False

    return True


dy = [0,0,-1,1]
dx = [1,-1,0,0]        

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(input())
    arr.append(arr1)

sy,sx = map(int, input().split())
ey,ex = map(int, input().split())

sy -= 1
sx -= 1
ey -= 1
ex -= 1


ss = bfs()

if ss == False:
    print('YES')
else:
    print('NO')
```

![20210510_070853](20210510_070853.png)
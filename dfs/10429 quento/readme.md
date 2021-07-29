[ 백준 : quento ] (https://www.acmicpc.net/problem/10429)



- 단순한 dfs문제
- 하나만 찾을경우 flag로 나와버리는 설정을 안해줬음에도 불구하고 나쁘지 않은 시간결과값을 얻었다.



```python
import sys
sys.stdin = open('10429.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy

def dfs(y,x,cnt,val,p_m):
    global n,m,arr,visit,stack_pos,answer

    if cnt == m:
        if val == n:
            answer = deepcopy(stack_pos)
        return

    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<3 and 0<=nx<3:
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                cnt += 1
                if cnt % 2 == 0:
                    if arr[ny][nx] == '+':
                        tmp = deepcopy(p_m)
                        p_m = 1
                    else:
                        tmp = deepcopy(p_m)
                        p_m = -1
                    stack_pos.append([ny,nx])
                    dfs(ny,nx,cnt,val,p_m)
                    stack_pos.pop()
                    p_m = deepcopy(tmp)
                else:
                    if p_m == 1:
                        val += arr[ny][nx]
                        stack_pos.append([ny,nx])
                        dfs(ny,nx,cnt,val,p_m)
                        stack_pos.pop()
                        val -= arr[ny][nx]
                    else:
                        val -= arr[ny][nx]
                        stack_pos.append([ny,nx])
                        dfs(ny,nx,cnt,val,p_m)
                        stack_pos.pop()
                        val += arr[ny][nx]
                cnt -= 1
                visit[ny][nx] = 0




    return





dy = [1,0,0,-1]
dx = [0,1,-1,0]
n,m = map(int, input().split())
m *= 2
m -= 1

arr = []
for _ in range(3):
    ar = list(input())
    arr.append(ar)

for y in range(3):
    for x in range(3):
        if arr[y][x] != '-' and arr[y][x]!= '+':
            arr[y][x] = int(arr[y][x])

visit = [[0]*3 for _ in range(3)]
# stack = []
stack_pos = []
answer = None

for y in range(3):
    for x in range(3):
        if y == 0:
            if x == 0 or x == 2:
                visit[y][x] = 1
                # stack.append(arr[y][x])
                stack_pos.append([y,x])
                dfs(y,x,1,arr[y][x],0)
                stack_pos.pop()
                # stack.pop()
                visit[y][x] = 0
        elif y == 1:
            if x == 1:
                visit[y][x] = 1
                # stack.append(arr[y][x])
                stack_pos.append([y,x])
                dfs(y,x,1,arr[y][x],0)
                stack_pos.pop()
                # stack.pop()
                visit[y][x] = 0
        else:
            if x == 0 or x == 2:
                visit[y][x] = 1
                # stack.append(arr[y][x])
                stack_pos.append([y,x])
                dfs(y,x,1,arr[y][x],0)
                stack_pos.pop()
                # stack.pop()
                visit[y][x] = 0

if answer == None:
    print(0)
else:
    print(1)
    for pos in answer:
        print('{} {}'.format(pos[0],pos[1]))
```

![20210727_201506](20210727_201506.png)


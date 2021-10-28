[ 백준 : 암벽 등반 ] (https://www.acmicpc.net/problem/2412)



- 롤드컵 보면서 매우 빠르게 쉽게 푼 문제
- bfs문제이다.
- 다만 조심해야할 점은 모든 홈을 메모리에 2차원 배열로 저장하려면 메모리 초과가 날거 같아서 객체 형태로 저장했다.



```python
import sys
sys.stdin = open('2412.txt','r')
from collections import deque
input = sys.stdin.readline


n,t = map(int, input().split())
visit = [0]*n
obj = {}

cnt = 0
for _ in range(n):
    x,y = map(int,input().split())
    value = obj.get(x)
    if value == None:
        obj[x] = {}
        obj[x][y] = cnt
    else:
        if y not in obj[x]:
            obj[x][y] = cnt

    cnt += 1


answer = -1

q = deque()
q.append([0,0,0])


while q:
    cnt,x,y = q.popleft()

    if y>=t:
        answer = cnt
        break

    for nxt_x in range(x-2,x+3):
        if 0<=nxt_x<=1000000 and nxt_x in obj:
            for nxt_y in range(y-2,y+3):
                if 0<=nxt_y<=t and nxt_y in obj[nxt_x]:
                    if visit[obj[nxt_x][nxt_y]] == 0:
                        visit[obj[nxt_x][nxt_y]] = 1
                        q.append([cnt+1,nxt_x,nxt_y])

print(answer)
```

![20211023_224906](20211023_224906.png)
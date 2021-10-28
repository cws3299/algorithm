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
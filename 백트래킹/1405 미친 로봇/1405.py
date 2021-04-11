import sys
sys.stdin = open('1405.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy

def dfs(y,x,move):
    global visit, percent , nn, e,w,s,n,stack,answer

    # print(y,x,move)

    if move > nn:
        return


    value = 1
    for st in stack:
        value *= st
    value = value/(100**move)
    percent[y][x] = deepcopy(value)


    if move == nn:
        answer += value
        # print(y,x,move,stack,answer)
        return

    

    for k in range(4):
        if k == 0:
            if visit[y][x+1] == 0:
                visit[y][x+1] = 1 
                stack.append(e)
                move += 1
                dfs(y,x+1,move)
                visit[y][x+1] = 0
                stack.pop()
                move -= 1
        elif k == 1:
            if visit[y][x-1] == 0:
                visit[y][x-1] = 1
                move += 1
                stack.append(w)
                dfs(y,x-1,move)
                visit[y][x-1] = 0
                stack.pop()
                move -= 1
        elif k == 2:
            if visit[y+1][x] == 0:
                visit[y+1][x] = 1
                move += 1
                stack.append(s)
                dfs(y+1,x,move)
                visit[y+1][x] = 0
                stack.pop()
                move -= 1
        elif k == 3:
            if visit[y-1][x] == 0:
                visit[y-1][x] = 1
                move += 1
                stack.append(n)
                dfs(y-1,x,move)
                visit[y-1][x] = 0
                stack.pop()
                move -= 1
    return

visit = [[0]*29 for _ in range(29)]
percent = [[0]*29 for _ in range(29)]
stack = []

nn,e,w,s,n = map(int, input().split())

answer = 0

visit[14][14] = 2
dfs(14,14,0)

ans = format(answer,".10f")
ans = str(ans)
# print(ans)
ll = len(ans)
answer =''
ss = len(ans)
for k in range(ll-1,-1,-1):
    if ans[k] == '0':
        ss -= 1
    else:
        break

print(ans[0:ss])

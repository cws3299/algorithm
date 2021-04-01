import sys
sys.stdin = open('9944.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy

def dfs(y,x,depth,cnt):
    global n,m,arr,visit,total,answer

    if cnt == total:
        if depth < answer:
            answer = depth
        return

    if depth >= answer:
        return

    for k in range(4):
        ny,nx,plus_cnt= move(y,x,dy[k],dx[k],depth)
        if plus_cnt == 0:
            continue
        depth += 1
        cnt += plus_cnt
        dfs(ny,nx,depth,cnt)
        depth -= 1
        reset(depth,plus_cnt)
        cnt -= plus_cnt

    return

def move(y,x,dy,dx,depth):
    global n,m,arr,visit,total,answer

    plus = 0
    ny = y
    nx = x
    while True:
        ny += dy
        nx += dx
        if ny<0 or n<=ny or nx<0 or m<=nx or arr[ny][nx] == '*' or visit[ny][nx] != -1:
            ny -= dy
            nx -= dx
            break
        visit[ny][nx] = depth
        plus += 1
    return ny,nx,plus

def reset(depth,plus):
    global n,m,visit

    # print(depth,plus)

    cnt = 0
    for y in range(n):
        stop = False
        for x in range(m):
            if visit[y][x] == depth:
                visit[y][x] = -1
                cnt += 1
            
            if cnt == plus:
                stop = True
                break
        if stop == True:
            break
    return

tc = 1
while True:
    try: 
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        n,m = map(int,input().split())
        arr = []
        for _ in range(n):
            arr1 = list(input())
            arr.append(arr1)

        total = 0
        answer = 100000000

        for y in range(n):
            for x in range(m):
                if arr[y][x] == '.':
                    total += 1

        visit = [[-1]*m for _ in range(n)]

        for y in range(n):
            for x in range(m):
                if arr[y][x] == '.':
                    visit[y][x] = -2
                    dfs(y,x,0,1)
                    # print('--------------------------------------------',y,x)
                    visit[y][x] = -1

        # print(answer)
        if answer == 100000000:
            print('Case {}: {}'.format(tc,-1))
        else:
            print('Case {}: {}'.format(tc,answer))
        tc += 1
    except:
        break
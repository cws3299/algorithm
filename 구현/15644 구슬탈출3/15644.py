import sys
sys.stdin = open('15644.txt','r')
from collections import deque
from copy import deepcopy

def bfs():
    global n,m,arr,visit,ry,rx,by,bx,oy,ox,answer,answer_lst

    q = deque()
    lst = []
    q.append([ry,rx,by,bx,1,lst])
    visit[ry][rx][by][bx] = 1


    stop = True
    while q:
        ryy,rxx,byy,bxx,cnt,lstt = q.popleft()

        if cnt > 10:
            break


        for k in range(4):
            new_ry,new_rx,r_move = move(ryy,rxx,dy[k],dx[k])
            new_by,new_bx,b_move = move(byy,bxx,dy[k],dx[k])

            if arr[new_by][new_bx] == 'O':
                continue
                
            if arr[new_ry][new_rx] == 'O':
                lstt.append(k)
                answer = cnt
                answer_lst = lstt
                stop = False
                break

            
            if new_ry == new_by and new_rx == new_bx:
                if r_move > b_move:
                    new_ry -= dy[k]
                    new_rx -= dx[k]
                elif b_move > r_move:
                    new_by -= dy[k]
                    new_bx -= dx[k]

            temp = deepcopy(lstt)
            if visit[new_ry][new_rx][new_by][new_bx] == False:
                visit[new_ry][new_rx][new_by][new_bx] = True
                temp.append(k)
                q.append([new_ry,new_rx,new_by,new_bx,cnt+1,temp])

        if stop == False:
            break
    return

def move(y,x,dyy,dxx):
    global n,m,arr

    move = 0
    ny = y
    nx = x

    while True:
        ny += dyy
        nx += dxx
        move += 1

        if arr[ny][nx] == '#':
            ny -= dyy
            nx -= dxx
            move -= 1
            break
        elif arr[ny][nx] == 'O':
            break

    return ny,nx,move

dy = [-1,1,0,0]
dx = [0,0,-1,1]
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(input())
    arr.append(arr1)

visit = [[[[False]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]

ry,rx,by,bx,oy,ox = None,None,None,None,None,None

for y in range(n):
    for x in range(m):
        if arr[y][x] == 'R':
            ry = y
            rx = x
        if arr[y][x] == 'B':
            by = y
            bx = x
        if arr[y][x] == 'O':
            oy = y
            ox = x

answer = 9876543210
answer_lst = deque()

bfs()
if answer == 9876543210:
    print(-1)
else:
    print(answer)
    # print(answer_lst)
    final_lst = []
    for ans in answer_lst:
        if ans == 0:
            final_lst.append('U')
        elif ans == 1:
            final_lst.append('D')
        elif ans == 2:
            final_lst.append('L')
        elif ans == 3:
            final_lst.append('R')
    for ans in final_lst:
        print(ans, end="")
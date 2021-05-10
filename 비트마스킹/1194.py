import sys
sys.stdin = open('1194.txt','r')
from collections import deque
from copy import deepcopy

def bfs(sy,sx):
    global INF,n,m,arr,visit,answer

    q = deque()
    q.append([sy,sx,1<<0,0])
    visit[sy][sx][1<<0] = 1

    while q:
        y,x,bit,move = q.popleft()
        
        if arr[y][x] == '1':
            answer = move
            break

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == '#':
                    pass
                elif arr[ny][nx] == '.' or arr[ny][nx] == '0' or arr[ny][nx] == '1':
                    tmp = deepcopy(bit)
                    if visit[ny][nx][tmp] == INF:
                        visit[ny][nx][tmp] = 1
                        q.append([ny,nx,tmp,move+1])
                elif arr[ny][nx] == 'a':
                    if not bit&(1<<1):
                        temp = deepcopy(bit)
                        tmp = (temp|(1<<1))
                    # print('+++++++++',bit)
                        if visit[ny][nx][tmp] == INF:
                            visit[ny][nx][tmp] = 1 
                            q.append([ny,nx,tmp,move+1])
                    else:
                        if visit[ny][nx][bit] == INF:
                                visit[ny][nx][bit] = 1 
                                q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'b':
                    if not bit&(1<<2):
                        temp = deepcopy(bit)
                        tmp = (temp|(1<<2))
                        if visit[ny][nx][tmp] == INF:
                            visit[ny][nx][tmp] = 1 
                            q.append([ny,nx,tmp,move+1])
                    else:
                        if visit[ny][nx][bit] == INF:
                                visit[ny][nx][bit] = 1 
                                q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'c':
                    if not bit&(1<<3):
                        temp = deepcopy(bit)
                        tmp = (temp|(1<<3))
                        if visit[ny][nx][tmp] == INF:
                            visit[ny][nx][tmp] = 1 
                            q.append([ny,nx,tmp,move+1])
                    else:
                        if visit[ny][nx][bit] == INF:
                                visit[ny][nx][bit] = 1 
                                q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'd':
                    if not bit&(1<<4):
                        temp = deepcopy(bit)
                        tmp = (temp|(1<<4))
                        if visit[ny][nx][tmp] == INF:
                            visit[ny][nx][tmp] = 1  
                            q.append([ny,nx,tmp,move+1])
                    else:
                        if visit[ny][nx][bit] == INF:
                                visit[ny][nx][bit] = 1 
                                q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'e':
                    if not bit&(1<<5):
                        temp = deepcopy(bit)
                        tmp = (temp|(1<<5))
                        if visit[ny][nx][tmp] == INF:
                            visit[ny][nx][tmp] = 1  
                            q.append([ny,nx,tmp,move+1])
                    else:
                        if visit[ny][nx][bit] == INF:
                                visit[ny][nx][bit] = 1 
                                q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'f':
                    if not bit&(1<<6):
                        temp = deepcopy(bit)
                        tmp = (temp|(1<<6))
                        if visit[ny][nx][tmp] == INF:
                            visit[ny][nx][tmp] = 1 
                            q.append([ny,nx,tmp,move+1])
                    else:
                        if visit[ny][nx][bit] == INF:
                                visit[ny][nx][bit] = 1 
                                q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'A':
                    if bit&(1<<1):
                        arr[ny][nx] == '.'
                        if visit[ny][nx][bit] == INF:
                            visit[ny][nx][bit] = 1
                            q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'B':
                    if bit&(1<<2):
                        arr[ny][nx] == '.'
                        if visit[ny][nx][bit] == INF:
                            visit[ny][nx][bit] = 1
                            q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'C':
                    if bit&(1<<3):
                        arr[ny][nx] == '.'
                        if visit[ny][nx][bit] == INF:
                            visit[ny][nx][bit] = 1
                            q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'D':
                    if bit&(1<<4):
                        arr[ny][nx] == '.'
                        if visit[ny][nx][bit] == INF:
                            visit[ny][nx][bit] = 1
                            q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'E':
                    if bit&(1<<5):
                        arr[ny][nx] == '.'
                        if visit[ny][nx][bit] == INF:
                            visit[ny][nx][bit] = 1
                            q.append([ny,nx,bit,move+1])
                elif arr[ny][nx] == 'F':
                    if bit&(1<<6):
                        arr[ny][nx] == '.'
                        if visit[ny][nx][bit] == INF:
                            visit[ny][nx][bit] = 1
                            q.append([ny,nx,bit,move+1])
        
    return

dy = [0,0,-1,1]
dx = [1,-1,0,0]
INF = sys.maxsize
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(input())
    arr.append(arr1)

visit =[[[INF]*(1<<7) for _ in range(m)]for _ in range(n)]

answer = False
for y in range(n):
    for x in range(m):
        if arr[y][x] == '0':
            bfs(y,x)

if answer == False:
    print(-1)
else:
    print(answer)
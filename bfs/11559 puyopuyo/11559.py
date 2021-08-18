import sys
sys.stdin = open('11559.txt','r')
from copy import deepcopy
from collections import deque

def pang():
    global arr,visit,delete_lst

    flag = False

    for y in range(12):
        for x in range(6):
            if arr[y][x] != '.':
                if visit[y][x] == 0:
                    visit[y][x] = 1

                    de_lst = [[y,x]]

                    q = deque()
                    q.append([y,x,arr[y][x]])
                    cnt = 1

                    while q:
                        y,x,g = q.popleft()

                        for k in range(4):
                            ny = y+dy[k]
                            nx = x+dx[k]
                            if 0<=ny<12 and 0<=nx<6:
                                if arr[ny][nx] == g:
                                    if visit[ny][nx] == 0:
                                        visit[ny][nx] = 1
                                        q.append([ny,nx,g])
                                        de_lst.append([ny,nx])
                                        cnt += 1
                    
                    if cnt >= 4:
                        flag = True
                        delete_lst += de_lst

    for de in delete_lst:
        y,x = de[0],de[1]
        arr[y][x] = '.'



    if flag == False:
        return False
    else:
        return True

def down():
    global arr,visit

    for x in range(6):
        for y in range(11,-1,-1):
            if arr[y][x] != '.':
                if 0<=y+1<12:
                    while y+1<12 and arr[y+1][x] == '.':
                        arr[y+1][x] = arr[y][x]
                        arr[y][x] = '.'
                        y += 1

    return



dy = [0,0,-1,1]
dx = [1,-1,0,0]
arr = []
answer = 0
visit = [[0]*6 for _ in range(12)]
for _ in range(12):
    ar = list(input())
    arr.append(ar)

while True:

    visit = [[0]*6 for _ in range(12)]
    delete_lst = []
    result = pang()
    if result == True:
        answer += 1
        down()
    else:
        break

print(answer)


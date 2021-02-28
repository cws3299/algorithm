import sys
sys.stdin = open('2573.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy
from collections import deque

def melting(ic):
    global n,m,arr,ice,ice_nm,temp,visit,lst

    cntt = 0
    for k in range(4):
        ny = ic[1]+dy[k]
        nx = ic[2]+dx[k]
        if 0<=ny<n and 0<=nx<m:
            if arr[ny][nx] == 0:
                cntt += 1

    temp[ic[1]][ic[2]] = arr[ic[1]][ic[2]] - cntt

    if temp[ic[1]][ic[2]] <= 0:
        temp[ic[1]][ic[2]] = 0
        lst.append(ic)

    return


def confirm(ic):
    global n,m,arr,ice,ice_nm,temp,visit,lst

    q = deque()
    q.append([ic[1],ic[2]])
    visit[ic[1]][ic[2]] = 1

    ct = 1

    while q:
        y,x = q.popleft()

        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if visit[ny][nx] ==0 and arr[ny][nx] > 0:
                    visit[ny][nx] = 1
                    ct += 1
                    q.append([ny,nx])

    return ct


dy = [0,0,-1,1]
dx = [1,-1,0,0]
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

ice = []
ice_nm = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] != 0:
            ice.append([ice_nm,y,x])
            ice_nm += 1

temp = deepcopy(arr)
lst = []

visit = [[0]*m for _ in range(n)]

# print(ice)
cnt = 1
ll = len(ice)
while True:
    # print(cnt)
    for ic in range(ll):
        melting(ice[ic]) # 얼음 하나씩 녹이기

    if len(ice) == 0:
        cnt = 0
        break

    for ls in lst:
        ice.remove(ls)
        ice_nm -= 1

    lst = []
    arr = deepcopy(temp)

    for ic in ice:
        length = confirm(ic) # 두 덩어리인지 확인하기
        break

    if length < ice_nm:
        break





    visit = [[0]*m for _ in range(n)]
    cnt += 1
    ll = len(ice)

print(cnt)
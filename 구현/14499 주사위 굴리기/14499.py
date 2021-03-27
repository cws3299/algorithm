import sys
sys.stdin = open('14499.txt','r')
from copy import deepcopy

def turning_south():
    global n,m,sy,sx,o,arr,orders,original_dice,new_dice

    new_dice[1] = original_dice[5]
    new_dice[2] = original_dice[1]
    new_dice[3] = original_dice[3]
    new_dice[4] = original_dice[4]
    new_dice[5] = original_dice[6]
    new_dice[6] = original_dice[2]

    original_dice = deepcopy(new_dice)
    return

def turning_north():
    global n,m,sy,sx,o,arr,orders,original_dice,new_dice

    new_dice[1] = original_dice[2]
    new_dice[2] = original_dice[6]
    new_dice[3] = original_dice[3]
    new_dice[4] = original_dice[4]
    new_dice[5] = original_dice[1]
    new_dice[6] = original_dice[5]

    original_dice = deepcopy(new_dice)
    return

def turning_west():
    global n,m,sy,sx,o,arr,orders,original_dice,new_dice

    new_dice[1] = original_dice[4]
    new_dice[2] = original_dice[2]
    new_dice[3] = original_dice[1]
    new_dice[4] = original_dice[6]
    new_dice[5] = original_dice[5]
    new_dice[6] = original_dice[3]

    original_dice = deepcopy(new_dice)
    return

def turning_east():
    global n,m,sy,sx,o,arr,orders,original_dice,new_dice

    new_dice[1] = original_dice[3]
    new_dice[2] = original_dice[2]
    new_dice[3] = original_dice[6]
    new_dice[4] = original_dice[1]
    new_dice[5] = original_dice[5]
    new_dice[6] = original_dice[4]

    original_dice = deepcopy(new_dice)
    return

def color():
    global n,m,sy,sx,o,arr,orders,original_dice,new_dice

    if arr[sy][sx] == 0:
        arr[sy][sx] = original_dice[1]
    else:
        original_dice[1] = arr[sy][sx]
        arr[sy][sx] = 0

    return



n,m,sy,sx,o = map(int, input().split())
arr = []
for _ in range(n):
    arr1 =list(map(int, input().split()))
    arr.append(arr1)

orders = list(map(int, input().split()))

original_dice = [0,0,0,0,0,0,0]
new_dice = [0,0,0,0,0,0,0]

cnt = 0
ll = len(orders)

# 1,2,3,4 => 동,서,북,남
# 주사위 굴려서 방향바꾸기
# 숫자 입히기
# 출력하기

cnt = 0
while cnt<ll:
    turn = orders[cnt]
    # print('---',cnt,turn)

    if turn == 4:
        ny = sy+1
        nx = sx
        if 0<=ny<n and 0<=nx<m:
            sy = ny
            sx = nx
            turning_south()
            new_dice = [0,0,0,0,0,0,0]
            color()
            print(original_dice[6])
    if turn == 3:
        ny = sy-1
        nx = sx
        if 0<=ny<n and 0<=nx<m:
            sy = ny
            sx = nx
            turning_north()
            new_dice = [0,0,0,0,0,0,0]
            color()
            print(original_dice[6])
    if turn == 2:
        ny = sy
        nx = sx-1
        if 0<=ny<n and 0<=nx<m:
            sy = ny
            sx = nx
            turning_west()
            new_dice = [0,0,0,0,0,0,0]
            color()
            print(original_dice[6])
    if turn == 1:
        ny = sy
        nx = sx+1
        if 0<=ny<n and 0<=nx<m:
            sy = ny
            sx = nx
            turning_east()
            new_dice = [0,0,0,0,0,0,0]
            color()
            print(original_dice[6])

    cnt += 1




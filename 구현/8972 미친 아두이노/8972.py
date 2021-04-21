import sys
sys.stdin = open('8972.txt','r')
from collections import deque

def moveMe(d):
    global n,m,arr,robots,my,mx

    for k in range(1,10):
        if k == d:
            ny = my+dy[k]
            nx = mx+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] != 'R':
                    arr[my][mx] = '.'
                    arr[ny][nx] = 'I'
                    my = ny
                    mx = nx
                    return True

    return False

def moveRobots():
    global n,m,arr,robots,my,mx,many

    lst = set()
    destroy = set()

    while robots:
        y,x = robots.popleft()

        gy = 1000000
        gx = 1000000
        gg = 1000000000
        for k in range(8):
            ny = y+ry[k]
            nx = x+rx[k]
            if abs(my-ny)+abs(mx-nx) < gg:
                gy = ny
                gx = nx 
                gg = abs(my-ny)+abs(mx-nx)
        if arr[gy][gx] == 'I':
            return False
        lst.add((gy,gx))
        arr[y][x] = '.'
        arr[gy][gx] = 'R'
        many[gy][gx] += 1
        if many[gy][gx] > 1:
            destroy.add((gy,gx))

    for ls in lst:
        many[ls[0]][ls[1]] = 0


    for de in destroy:
        arr[de[0]][de[1]] = '.'
        lst.remove((de[0],de[1]))


    for ls in lst:
        robots.append([ls[0],ls[1]])
        arr[ls[0]][ls[1]] = 'R'

    # for ar in arr:
    #     for a in ar:
    #         print(a, end='')
    #     print()

    return True


ry = [1,1,1,0,0,-1,-1,-1]
rx = [-1,0,1,-1,1,-1,0,1]

dy = [0,1,1,1,0,0,0,-1,-1,-1]
dx = [0,-1,0,1,-1,0,1,-1,0,1]
n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr1 = list(input())
    arr.append(arr1)

many = [[0]*m for _ in range(n)]

moving = list(map(int, input()))

move = deque()
for mo in moving:
    move.append(mo)

robots = deque()
my,mx = None, None

for y in range(n):
    for x in range(m):
        if arr[y][x] == 'R':
            robots.append([y,x])
        if arr[y][x] == 'I':
            my = y
            mx = x

cnt = 1
answer = True
while move:
    d = move.popleft()

    result_Me = moveMe(d)

    if result_Me == False:
        print("kraj {0}".format(cnt))
        answer = False
        break
    
    # print('-----------------------------------')
    result_robots = moveRobots()

    if result_robots == False:
        print("kraj {0}".format(cnt))
        answer = False
        break

    cnt += 1

if answer == True:
    for ar in arr:
        for a in ar:
            print(a, end='')
        print()


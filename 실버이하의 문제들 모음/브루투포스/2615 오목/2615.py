import sys
sys.stdin = open('2615.txt','r')

def five(y,x,a):
    global arr,visit

    ## 가로 오른쪽
    g = 0
    for k in range(x,19):
        if 0<=k<19:
            if arr[y][k] == a:
                g += 1
            else:
                break

    ## 가로 왼쪽
    for k in range(x-1,-1,-1):
        if 0<=k<19:
            if arr[y][k] == a:
                g += 1
            else:
                break
    
    ## 세로 아래
    s = 0
    for k in range(y,19):
        if 0<=k<19:
            if arr[k][x] == a:
                s += 1
            else:
                break

    ## 세로 위
    for k in range(y-1,-1,-1):
        if 0<=k<19:
            if arr[k][x] == a:
                s += 1
            else:
                break

    # 오른쪽 대각선 아래
    r = 0
    k = 0
    while 0<=y+k<19 and 0<=x+k<19:
        if arr[y+k][x+k] == a:
            r += 1
            k += 1
        else:
            break

    # 왼쪽 대각선 위
    # print(r)
    k = 1
    while 0<=y-k<19 and 0<=x-k<19:
        if arr[y-k][x-k] == a:
            r += 1
            k += 1
        else:
            break

    # 왼쪽 대각선 아래
    l = 0
    k = 0
    while 0<=y+k<19 and 0<=x-k<19:
        if arr[y+k][x-k] == a:
            l += 1
            k += 1
        else:
            break

    # 오른쪽 대각선 위
    k = 1
    while 0<=y-k<19 and 0<=x+k<19:
        if arr[y-k][x+k] == a:
            l += 1
            k += 1
        else:
            break

    
    # print(y,x,g,s,r,l)

    
    if (g == 5 or s == 5 or r == 5 ) and not (g >=6 and s >=6 and r >=6 and l >=6) :
        return 1
    elif (l == 5 ) and not (g >=6 and s >=6 and r >=6 and l >=6) :
        return 2
    else:
        return False



arr = []
visit = [[0]*19 for _ in range(19)]
for _ in range(19):
    ar = list(map(int, input().split()))
    arr.append(ar)

for y in range(19):
    flag = True
    for x in range(19):
        if arr[y][x] != 0:
            result = five(y,x,arr[y][x])
            if result == 1:
                print(arr[y][x])
                print('{} {}'.format(y+1,x+1))
                flag = False
                break
            if result == 2:
                print(arr[y][x])
                print('{} {}'.format(y+5,x-3))
                flag = False
                break
    if flag == False:
        break

if flag == True:
    print(0)
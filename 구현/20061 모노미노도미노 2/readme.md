[백준 : 모노미노 도미노2] (https://www.acmicpc.net/problem/20061)



- 상당히 어려웠던 구현문제....
- 하지만 풀었당!!!! 헤헤



```python
import sys
sys.stdin = open('20061.txt','r')

def down_crush(num):
    global arr

    if num == 1:
        for x in range(0,4):
            for y in range(9,4,-1):
                arr[y][x] = arr[y-1][x]
    if num == 2:
        c = 0
        while c<2:
            if c == 0:
                for x in range(0,4):
                    for y in range(9,3,-1):
                        arr[y][x] = arr[y-1][x]
            if c == 1:
                for x in range(0,4):
                    for y in range(9,4,-1):
                        arr[y][x] = arr[y-1][x]

            c += 1
    return



def down_check():
    global arr

    lst = [0,0,0,0]

    for y in range(4,6):
        for x in range(0,4):
            if arr[y][x] == 1:
                lst[x] += 1

    if sum(lst) == 0:
        return

    down_crush(max(lst))
    return

def down_bomb():
    global n,arr

    lst = []

    for y in range(6,10):
        check = 0
        for x in range(0,4):
            if arr[y][x] == 1:
                check += 1
        if check == 4:
            lst.append(y)

    if len(lst) == 0:
        return
    down_real_bomb(lst)
    return

def down_real_bomb(lst):
    global n,arr,answer

    answer += len(lst)

    while True:
        k = lst.pop()

        for x in range(0,4):
            for y in range(k,4,-1):
                arr[y][x] = arr[y-1][x]

        if len(lst) > 0:
            for k in range(len(lst)):
                lst[k] += 1
        else:
            return

def down(t,y,x):
    global n,arr

    if t == 1:
        y = 4
        
        while True:
            if y == 9:
                arr[y][x] = 1
                break
            elif y <= 8 and arr[y+1][x] == 0:
                y += 1
            else:
                arr[y][x] = 1
                break
    
    if t == 3:
        y == 5 # x=x , y=4,5

        while True:
            if y == 9:
                arr[y-1][x] = 1
                arr[y][x] = 1
                break
            elif arr[y+1][x] == 0 and y <= 8:
                y += 1
            else:
                arr[y-1][x] = 1
                arr[y][x] = 1
                break

    if t == 2:
        y = 4 # x=x,x+1

        while True:
            if y == 9:
                arr[y][x] = 1
                arr[y][x+1] = 1
                break
            elif arr[y+1][x] == 0 and arr[y+1][x+1] ==0 and y<=8:
                y += 1
            else:
                arr[y][x] = 1
                arr[y][x+1] = 1
                break

    down_bomb()
    down_check()
    return

def right(t,y,x):
    global n,arr

    if t == 1:
        x = 4
        
        while True:
            if x == 9:
                arr[y][x] = 1
                break
            elif x <= 8 and arr[y][x+1] == 0:
                x += 1
            else:
                arr[y][x] = 1
                break
    
    if t == 3: # 아래로 긴거
        x == 4 # x=x , y=4,5

        while True:
            if x == 9:
                arr[y][x] = 1
                arr[y+1][x] = 1
                break
            elif arr[y+1][x+1] == 0 and arr[y][x+1] == 0 and x <= 8:
                x += 1
            else:
                arr[y][x] = 1
                arr[y+1][x] = 1
                break

    if t == 2: # 옆으로 긴거
        x = 5 # x=x,x+1

        while True:
            if x == 9:
                arr[y][x-1] = 1
                arr[y][x] = 1
                break
            elif arr[y][x+1] == 0 and x<=8:
                x += 1
            else:
                arr[y][x-1] = 1
                arr[y][x] = 1
                break

    right_bomb()
    right_check()
    return

def right_crush(num):
    global arr

    if num == 1:
        for y in range(0,4):
            for x in range(9,4,-1):
                arr[y][x] = arr[y][x-1]
    if num == 2:
        c = 0
        while c<2:
            if c == 0:
                for y in range(0,4):
                    for x in range(9,3,-1):
                        arr[y][x] = arr[y][x-1]
            if c == 1:
                for y in range(0,4):
                    for x in range(9,4,-1):
                        arr[y][x] = arr[y][x-1]
            c += 1
    return



def right_check():
    global arr

    lst = [0,0,0,0]

    for x in range(4,6):
        for y in range(0,4):
            if arr[y][x] == 1:
                lst[y] += 1

    if sum(lst) == 0:
        return

    right_crush(max(lst))
    return

def right_bomb():
    global n,arr

    lst = []

    for x in range(6,10):
        check = 0
        for y in range(0,4):
            if arr[y][x] == 1:
                check += 1
        if check == 4:
            lst.append(x)

    if len(lst) == 0:
        return
    right_real_bomb(lst)
    return

def right_real_bomb(lst):
    global n,arr,answer

    answer += len(lst)

    while True:
        k = lst.pop()

        for y in range(0,4):
            for x in range(k,4,-1):
                arr[y][x] = arr[y][x-1]

        if len(lst) > 0:
            for k in range(len(lst)):
                lst[k] += 1
        else:
            return


n = int(input())
arr = [[0]*10 for _ in range(10)]

answer = 0
block = 0
for _ in range(n):
    t,y,x = map(int, input().split())
    down(t,y,x)
    right(t,y,x)

print(answer)

for k in range(10):
    for s in range(10):
        if arr[k][s] == 1:
            block += 1
print(block)
```

![20210614_175603](20210614_175603.png)
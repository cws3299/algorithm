import sys
sys.stdin = open('3190.txt','r')
from collections import deque

n = int(input())
arr = [[0]*n for _ in range(n)]
brr = [[0]*n for _ in range(n)]
apples = int(input())
for _ in range(apples):
    y,x = map(int, input().split())
    arr[y-1][x-1] = 1

m = int(input())
turns_dict = {}
turns_lst = deque()
for _ in range(m):
    time,dire = input().split()
    turns_dict[int(time)] = dire
    turns_lst.append(int(time))

snakes = deque()
snakes.append([0,0]) # 현재 뱀의 위치를 1차원 큐 리스트로 나타냄
brr[0][0] = 1 # 현재뱀의 위치를 2차원 배열로 나타냄

q = deque()
q.append([0,0,3,0])
answer = 0

# print(turns_lst)

# print(arr)
while True:
    y,x,d,time = q.pop()

    # for ar in arr:
    #     for a in ar:
    #         print(a , end= ' ')
    #     print()
    
    # print('------------------------------')

    # print(turns_lst)
    if turns_lst == 0:
        if d == 3:
            answer = time +(n-x)
        if d == 2:
            answer = time + (x+1)
        if d == 1:
            answer = time +(n-y)
        if d == 0:
            answer = time + (y+1)
        break
        

    if d == 3:
        ny = y
        nx = x+1
        if 0<=ny<n and 0<=nx<n: # 벽에 안 부딫히는 경우
            if brr[ny][nx] == 0:
                if arr[ny][nx] == 1: #사과인 경우
                    arr[ny][nx] = 0
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,0,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                        if new_d == 'D':
                            q.append([ny,nx,1,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                else: # 사과가 아닌 경우
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,0,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            # print(a,b)
                            brr[a][b] = 0
                        if new_d == 'D':
                            q.append([ny,nx,1,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            brr[a][b] = 0
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                        a,b = snakes.popleft()
                        brr[a][b] = 0
            else: # 자기 자신에 부딫히는 경우
                # print('------',ny,nx,brr[ny][nx])
                answer = time+1
                break

        else: # 벽에 부딫히는 경우
            # print('------')
            answer = time+1
            break
    
    if d == 2:
        ny = y
        nx = x-1
        if 0<=ny<n and 0<=nx<n: # 벽에 안 부딫히는 경우
            if brr[ny][nx] == 0:
                if arr[ny][nx] == 1: #사과인 경우
                    arr[ny][nx] = 0
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,1,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                        if new_d == 'D':
                            q.append([ny,nx,0,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                else: # 사과가 아닌 경우
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,1,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            brr[a][b] = 0
                        if new_d == 'D':
                            q.append([ny,nx,0,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            brr[a][b] = 0
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                        a,b = snakes.popleft()
                        brr[a][b] = 0
            else: # 자기 자신에 부딫히는 경우
                answer = time+1
                break

        else: # 벽에 부딫히는 경우
            answer = time+1
            break
    
    if d == 1:
        ny = y+1
        nx = x
        if 0<=ny<n and 0<=nx<n: # 벽에 안 부딫히는 경우
            if brr[ny][nx] == 0:
                if arr[ny][nx] == 1: #사과인 경우
                    arr[ny][nx] = 0
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,3,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                        if new_d == 'D':
                            q.append([ny,nx,2,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                else: # 사과가 아닌 경우
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,3,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            brr[a][b] = 0
                        if new_d == 'D':
                            q.append([ny,nx,2,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            brr[a][b] = 0
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                        a,b = snakes.popleft()
                        brr[a][b] = 0
            else: # 자기 자신에 부딫히는 경우
                answer = time +1
                break

        else: # 벽에 부딫히는 경우
            answer = time +1
            break

    if d == 0:
        ny = y-1
        nx = x
        if 0<=ny<n and 0<=nx<n: # 벽에 안 부딫히는 경우
            if brr[ny][nx] == 0: 
                if arr[ny][nx] == 1: #사과인 경우
                    arr[ny][nx] = 0
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,2,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                        if new_d == 'D':
                            q.append([ny,nx,3,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                else: # 사과가 아닌 경우
                    if time+1 in turns_lst: # 방향 바꾸는 경우
                        turns_lst.popleft()
                        new_d = turns_dict[time+1]
                        if new_d == 'L':
                            q.append([ny,nx,2,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            brr[a][b] = 0
                        if new_d == 'D':
                            q.append([ny,nx,3,time+1])
                            snakes.append([ny,nx])
                            brr[ny][nx] = 1
                            a,b = snakes.popleft()
                            brr[a][b] = 0
                    else:
                        q.append([ny,nx,d,time+1])
                        snakes.append([ny,nx])
                        brr[ny][nx] = 1
                        a,b = snakes.popleft()
                        brr[a][b] = 0
            else: # 자기 자신에 부딫히는 경우
                answer = time +1
                break

        else: # 벽에 부딫히는 경우
            answer = time +1
            break

    

print(answer)


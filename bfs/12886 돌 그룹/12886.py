import sys
sys.stdin = open('12886.txt','r')
from collections import deque
# from copy import deepcopy

a,b,c = map(int, input().split())
lst = set()

q = deque()
q.append([a,b,c])
lst.add((a,b,c))
answer = 0
# print(answer)
# visit = [[[0]*1001 for _ in range(1001)] for _ in range(1001)]
# visit[a][b][c] = 1
# print(visit)
while q:
    x,y,z = q.popleft()
    # print(x,y,z)

    # xx = deepcopy(x)
    # yy = deepcopy(y)
    # zz = deepcopy(z)

    if x == y and y == z:
        answer = 1
        break



    if x != y:
        if x > y:
            temp = (x-y,y+y,z)
            l1 = len(lst)
            lst.add(temp)
            l2 = len(lst)
            if l1 != l2:
                q.append(temp)
            # if temp not in lst:
            #     lst.append(temp)
            # if visit[x-y][y+y][z] == 0:
            #     visit[x-y][y+y][z] = 1
        else:
            temp = (x+x,y-x,z)
            l1 = len(lst)
            lst.add(temp)
            l2 = len(lst)
            if l1 != l2:
                q.append(temp)
            # if temp not in lst:
            #     lst.append(temp)
            #     q.append(temp)
            # if visit[x+x][y-x][z] == 0:
            #     visit[x+x][y-x][z] = 1

    if x != z:
        if x > z:
            temp = (x-z,y,z+z)
            l1 = len(lst)
            lst.add(temp)
            l2 = len(lst)
            if l1 != l2:
                q.append(temp)
            # if temp not in lst:
            #     lst.append(temp)
            #     q.append(temp)
            # if visit[x-z][y][z+z] == 0:
            #     visit[x-z][y][z+z] = 1
        else:
            temp = (x+x,y,z-x)
            l1 = len(lst)
            lst.add(temp)
            l2 = len(lst)
            if l1 != l2:
                q.append(temp)
            # if temp not in lst:
            #     lst.append(temp)
            #     q.append(temp)
            # if visit[x+x][y][z-x] == 0:
            #     visit[x+x][y][z-x] = 1

    if y != z:
        if y > z:
            temp = (x,y-z,z+z)
            l1 = len(lst)
            lst.add(temp)
            l2 = len(lst)
            if l1 != l2:
                q.append(temp)
            # if temp not in lst:
            #     lst.append(temp)
            #     q.append(temp)
            # if visit[x][y-z][z+z] == 0:
            #     visit[x][y-z][z+z] = 1
        else:
            temp = (x,y+y,z-y)
            l1 = len(lst)
            lst.add(temp)
            l2 = len(lst)
            if l1 != l2:
                q.append(temp)
            # if temp not in lst:
            #     lst.append(temp)
            #     q.append(temp)
            # if visit[x][y+y][z-y] == 0:
            #     visit[x][y+y][z-y] = 1

    
print(answer)

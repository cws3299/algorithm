import sys
sys.stdin = open('16947.txt','r')
sys.setrecursionlimit(10**5)
from copy import deepcopy

def search_circle(pre,now):
    global n , roads, state, visit,point,flag

    for nxt in roads[now]:
        if visit[nxt] == 0 and flag == False:
            visit[nxt] = 1
            search_circle(now,nxt)
            visit[nxt] = 0
        elif visit[nxt] == 1 and nxt != pre and flag == False:
            point = nxt
            flag = True
            state = deepcopy(visit)

    return


def setting(now,end):
    global n , roads, state, visit,point,flag

    for nxt in roads[now]:
        if visit[nxt] == 0 and flag == False:
            visit[nxt] = 1
            if nxt == end:
                flag = True
                return
            if state[nxt] == 1:
                state[nxt] = 0
            setting(nxt,end)
            visit[nxt] = 0
    return



def go(now,move):
    global n , roads, state, visit,point,flag,distance

    for nxt in roads[now]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            tmp = deepcopy(move)
            if state[nxt] == 1:
                move = 0
            else:
                move += 1
            distance[nxt] = move
            go(nxt,move)
            move = deepcopy(tmp)
            visit[nxt] = 0
    return



n = int(input())
roads = [[] for _ in range(n)]
state = [0]*n
visit = [0]*n
flag = False
point = None

for _ in range(n):
    a,b = map(int, input().split())
    roads[a-1].append(b-1)
    roads[b-1].append(a-1)

visit[0] = 1
search_circle(-1,0)
check = False
if point == 0:
    check = False
else:
    check = True

if check == True:
    visit = [0]*n
    visit[0] = 1
    flag = False
    state[0] = 0
    setting(0,point)

visit = [0]*n
distance = [0]*n

visit[point] = 1
distance[point] = 0
go(point,0)



for ans in distance:
    print(ans, end=' ')
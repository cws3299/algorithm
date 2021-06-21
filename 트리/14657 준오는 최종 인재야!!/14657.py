import sys
sys.stdin = open('14657.txt','r')
sys.setrecursionlimit(10**6)

def go1(now,depth,wt):
    global n,m,ans1,ans1_depth,visit,roads,ans1_wt

    # print('ans1',now,depth,wt)

    if ans1_depth <= depth:
        ans1_depth = depth
        if ans1_wt < wt or ans1_wt == 0:
            ans1_wt = wt
            ans1 = now

    for nxt,wtt in roads[now].items():
        if visit[nxt] == 0:
            visit[nxt] = 1
            depth += 1
            wt += wtt
            go1(nxt,depth,wt)
            wt -= wtt
            depth -= 1

    return

def go1_5(now,depth,wt):
    global n,m,ans1,ans1_depth,visit,roads,ans1_wt

    # print('ans1',now,depth,wt)

    if depth == ans1_depth:
        lst1.append([now,wt])

    for nxt,wtt in roads[now].items():
        if visit[nxt] == 0:
            visit[nxt] = 1
            depth += 1
            wt += wtt
            go1_5(nxt,depth,wt)
            wt -= wtt
            depth -= 1

    return

def go2(now,depth,wt):
    global n,m,ans2,ans2_depth,visit,roads,ans2_wt

    # print(now,depth,wt)


    if ans2_depth <= depth:
        ans2_depth = depth
        if ans2_wt < wt or ans2_wt == 0:
            ans2_wt = wt
            ans2 = now

    for nxt,wtt in roads[now].items():
        if visit[nxt] == 0:
            visit[nxt] = 1
            depth += 1
            wt += wtt
            go2(nxt,depth,wt)
            wt -= wtt
            depth -= 1

    return

def go2_5(now,depth,wt):
    global lst,ans2_depth,n,m,ans2,ans2_depth,visit,roads,ans2_wt

    
    # print(now,depth,wt)

    if depth == ans2_depth:
        lst.append([now,wt])


    for nxt,wtt in roads[now].items():
        if visit[nxt] == 0:
            visit[nxt] = 1
            depth += 1
            wt += wtt
            go2_5(nxt,depth,wt)
            wt -= wtt
            depth -= 1

    return

def go3(now,final,wt):
    global n,m,ans2,ans2_depth,visit,roads,wttt

    if now == final:
        wttt = wt


    for nxt,wtt in roads[now].items():
        if visit[nxt] == 0:
            visit[nxt] = 1
            wt += wtt
            go3(nxt,final,wt)
            visit[nxt] = 0
            wt -= wtt


    return






n,m = map(int, input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(n-1):
    a,b,w = map(int, input().split())
    roads[a][b] = w
    roads[b][a] = w

visit = [0]*(n+1)
ans1 = 0
ans1_depth = 0
ans1_wt = 0
visit[1] = 1
go1(1,0,0)

visit = [0]*(n+1)
visit[1] = 1
lst1 = []
go1_5(1,0,0)

# print(lst1)
lst1.sort(key=lambda lst1:(lst1[1]))

ans1 = lst1[0][0]
# print('ans1',ans1)

visit = [0]*(n+1)
ans2 = 0
ans2_depth = 0
ans2_wt = 0
visit[ans1] = 1
go2(ans1,0,0)

visit = [0]*(n+1)
visit[ans1] = 1
lst = []
go2_5(ans1,0,0)

wttt = 0
# print(lst)
lst.sort(key=lambda lst:(lst[1]))
ans2 = lst[0][0]

visit = [0]*(n+1)
go3(ans1,ans2,0)

# print(wttt)
   

s = wttt // m
ss = wttt%m

if ss != 0:
    s += 1

print(s)

import sys
sys.stdin = open('17940.txt','r')
import heapq

def dijkstra():
    global n,end,whose,road

    answer = [[float('inf'),float('inf')] for _ in range(n)]
    # answer_fee = [float('inf')]*(n)
    pq = []
    heapq.heappush(pq,[0,0,0,whose[0],0])
    answer[0][0] = 0
    # answer_fee[0]=0
    end_fee = float('inf')

    while pq:
        change,now,move,now_who,fee = heapq.heappop(pq)
        if change > answer[end][0]:
            break

        if now == end:
            if answer[end][0] >= change:
                if end_fee > fee:
                    end_fee = fee
            continue

        if answer[now][0] < change:
            continue

        for nxt, wt in road[now]:
            if whose[nxt] != now_who:
                if answer[nxt][0] > change + 1 :
                    answer[nxt][0] = change +1
                    answer[nxt][1] = fee+wt
                    heapq.heappush(pq,[change+1,nxt,move+1,whose[nxt],fee+wt])
                elif answer[nxt][0] == change + 1:
                    answer[nxt][0] = change +1
                    if answer[nxt][1] > fee+wt:
                        answer[nxt][1] = fee+wt
                        heapq.heappush(pq,[change+1,nxt,move+1,whose[nxt],fee+wt])
            else:
                if answer[nxt][0] > change:
                    answer[nxt][0] = change
                    answer[nxt][1] = fee+wt
                    heapq.heappush(pq,[change,nxt,move+1,now_who,fee+wt])
                elif answer[nxt][0] == change:
                    answer[nxt][0] = change
                    if answer[nxt][1] > fee+wt:
                        answer[nxt][1] = fee+wt
                        heapq.heappush(pq,[change,nxt,move+1,now_who,fee+wt])


    return [answer[end][0], end_fee]

n,end = map(int, input().split())
# road = [[] for _ in range(n)]
road = {node:[] for node in range(n)}
whose = []
for _ in range(n):
    w = int(input())
    whose.append(w)
cnt = 0
for s in range(n):
    lst = list(map(int, input().split()))
    # lst = lst[cnt:]
    for e in range(cnt,n):
        if lst[e] != 0:
            road[s].append([e,lst[e]])
            road[e].append([s,lst[e]])

    cnt += 1
    if cnt == n:
        break

answers = dijkstra()
for ans in answers:
    print(ans, end=' ')



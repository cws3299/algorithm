# 문제 풀이 날짜 : 2021.02.26

import sys
sys.stdin = open('13911.txt','r')
import heapq

def dijkstra_mc():
    global n,m,roads,space,mc_distance

    answer_mc = [float('inf')]*(n+1) # 각 주거지에서 맥도날드 까지의 거리 
    pq = []

    for start in range(1,n+1):
        if space[start] == 1 or space[start] == 3: # 맥도날드일 경우만 heapq에 넣어줌
            answer_mc[start] = 0
            heapq.heappush(pq,[answer_mc[start],start])

    while pq:
        dis,pos = heapq.heappop(pq)

        if answer_mc[pos] < dis or mc_distance<dis:
            continue

        for nxt,wt in roads[pos].items():
            distance = dis+wt
            if answer_mc[nxt] > distance and distance <= mc_distance:
                answer_mc[nxt] = distance
                heapq.heappush(pq,[answer_mc[nxt],nxt])


    return answer_mc # 최종적으로 맥세권거리안 집들의 맥도날드 거리가 출력

def dijkstra_sb():
    global n,m,roads,space,mc_distance

    answer_sb = [float('inf')]*(n+1) # 각 주거지에서 스타벅스 까지의 거리 
    pq = []

    for start in range(1,n+1):
        if space[start] == 2 or space[start] == 3: # 스타벅스일 경우만 heapq에 넣어줌
            answer_sb[start] = 0
            heapq.heappush(pq,[answer_sb[start],start])

    while pq:
        dis,pos = heapq.heappop(pq)

        if answer_sb[pos] < dis or sb_distance<dis:
            continue

        for nxt,wt in roads[pos].items():
            distance = dis+wt
            if answer_sb[nxt] > distance and distance <= sb_distance:
                answer_sb[nxt] = distance
                heapq.heappush(pq,[answer_sb[nxt],nxt])


    return answer_sb # 최종적으로 스세권거리안 집들의 스타벅스 거리가 출력


n,m = map(int, input().split())
roads = {node:{} for node in range(n+1)}
for _ in range(m):
    u,v,w = map(int, input().split())
    value = roads.get(u)
    vv = value.get(v)
    if vv == None or vv > w:   # 같은 정점을 연결하는 간선이 여러개 있을 수 있으므로
        roads[u][v] = w        # vv = None 일 경우 현재 간선 없으니 추가
        roads[v][u] = w        # vv가 있으나 w가 더 작을경우 더 빠른길이므로 길 바꿔주기

space = [0]*(n+1) # 일단 모두 집일경우 0으로 세팅
mc_cnt, mc_distance = map(int, input().split())
mc_positions = list(map(int, input().split()))

for mc in mc_positions:
    space[mc] = 1 # 맥도날드인 곳은 1로 세팅

sb_cnt, sb_distance = map(int, input().split())
sb_positions = list(map(int, input().split()))

for sb in sb_positions:
    if space[sb] == 0: # 주거지인 경우 스타벅스 2로 세팅
        space[sb] = 2
    elif space[sb] == 1:
        space[sb] = 3 # 맥도날드가 있는 곳에 스타벅스가 같이 생기는 경우 3 세팅

mc = dijkstra_mc()
sb = dijkstra_sb()

answer = 100000

for ans in range(n+1):
    if space[ans] == 0:
        if 0< mc[ans] <= mc_distance and 0< sb[ans] <= sb_distance:
            if answer > mc[ans] + sb[ans]:
                answer = mc[ans] + sb[ans]

if answer == 100000:
    print(-1) # 합당한 집이 없는 경우
else:
    print(answer)


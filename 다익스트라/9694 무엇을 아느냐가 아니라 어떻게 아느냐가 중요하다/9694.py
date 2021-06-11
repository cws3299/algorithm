import sys
sys.stdin = open('9694.txt','r')
import heapq

def dijkstra():
    global n,m,roads,flag

    answer = [float('inf')]*m
    pq = []
    answer[0] = 0
    heapq.heappush(pq,[answer[0],0])
    prev = [-1]*m

    while pq:
        distance , now = heapq.heappop(pq)

        if now == m-1:
            flag = True
            break

        if answer[now] < distance:
            continue

        for nxt, wt in roads[now].items():
            new_distance = distance + wt
            if answer[nxt] > new_distance:
                answer[nxt] = new_distance
                prev[nxt] = now
                heapq.heappush(pq,[answer[nxt],nxt])

    lst = [m-1]
    go = m-1
    if flag == True:
        while True:
            go = prev[go]
            lst.append(go)
            if go == 0:
                break
        
    # print(lst)    
    lst.reverse()
    return lst


t = int(input())
for tc in range(t):
    n,m = map(int, input().split())
    roads = {road:{} for road in range(m)}
    flag = False

    for _ in range(n):
        a,b,w = map(int ,input().split())
        value = roads.get(a)
        vv = value.get(b)
        if vv == None or w < vv:
            roads[a][b] = w
            roads[b][a] = w

    aa = dijkstra()

    if flag == False:
        print('Case #{}: -1'.format(tc+1))
    else:
        print('Case #{}: '.format(tc+1), end = '')
        for a in aa:
            print(a, end= ' ')
    print()


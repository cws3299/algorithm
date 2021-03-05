import sys
sys.stdin = open('2176.txt','r')
sys.setrecursionlimit(10**5)
import heapq

def dijkstra():
    global n,m,answer,roads

    pq = []
    answer[2] = 0
    heapq.heappush(pq,[answer[2],2])

    while pq:
        now_distance, now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt , wt in roads[now_position].items():
            distance = now_distance+wt

            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[answer[nxt],nxt])

    return

def go(now,distance):
    global n,m,answer,roads,dp

    if now == 2:
        return 1

    if dp[now] != 0:
        return dp[now]

    for nxt in roads[now].keys():
        if answer[nxt] < distance:
            dp[now] += go(nxt,answer[nxt])

    return dp[now]


n,m = map(int, input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(m):
    s,e,w = map(int, input().split())
    roads[s][e] = w
    roads[e][s] = w

answer = [float('inf')]*(n+1)

dijkstra()

dp = [0]*(n+1)

# print(roads)
# print(answer)
go(1,answer[1])

# print(dp)
print(dp[1])
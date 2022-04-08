import sys
sys.stdin = open('15808.txt','r')
import heapq

def dijkstra():

    answer = [-float('inf')] * (n+1) # 거리 , 어떤 start
    pq = []

    for p in range(1,n+1):
        if travelPositionList[p] != 0:
            answer[p] = travelPositionList[p]
            heapq.heappush(pq, [travelPositionList[p], p])

    while pq:
        nowValue, nowPosition = heapq.heappop(pq)

        if answer[nowPosition] > nowValue:
            continue

        for nxt in useEdges[nowPosition]:
            nxtValue = edges[nowPosition][nxt]
            if nxtValue != 0:
                value = nowValue - nxtValue
                if answer[nxt] < value:
                    answer[nxt] = value
                    heapq.heappush(pq, [value, nxt])

    final = 0
    for p in range(1,n+1):
        if housePositionList[p] != 0:
            answer[p] += housePositionList[p]
            if final < answer[p]:
                final = answer[p]

    return final

n = int(input())
edges = []
edges.append([0] * (n+1))
useEdges = []
useEdges.append([])
for k in range(1,n+1):
    edge = [0] + list(map(int, input().split()))
    edges.append(edge)
    temp = []
    for p in range(n+1):
        if edge[p] != 0:
            temp.append(p)
    useEdges.append(temp)

travelCnt , houseCnt = map(int, input().split())
travelPositionList = [0] * (n+1)
housePositionList = [0] * (n+1)

for _ in range(travelCnt):
    position, value = map(int,input().split())
    travelPositionList[position] = value

for _ in range(houseCnt):
    position, value = map(int,input().split())
    housePositionList[position] = value

print(dijkstra())
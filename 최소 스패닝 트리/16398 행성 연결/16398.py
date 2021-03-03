import sys
sys.stdin = open('16398.txt','r')
import heapq

def mst():
    global n,roads

    answer = [float('inf')]*(n+1)
    mst = [0]*(n+1)
    pq= []
    result = 0
    answer[1] = 0
    heapq.heappush(pq,[answer[1],1])

    while pq:
        now_distance , now_position = heapq.heappop(pq)

        # print(now_distance,now_position)

        if mst[now_position] != 0:
            continue

        result += now_distance
        mst[now_position] = 1

        for nxt,wt in roads[now_position].items():

            if mst[nxt] == 0 and answer[nxt] > wt:
                answer[nxt] = wt
                heapq.heappush(pq,[answer[nxt],nxt])

    # print(answer)
    # print(result)
    return result

n = int(input())
roads = {node:{} for node in range(n+1)}

for s in range(n):
    arr1 = list(map(int, input().split()))
    for e in range(n):
        w = arr1[e]
        roads[s+1][e+1] = w
        roads[e+1][s+1] = w

print(mst())

# print(roads)
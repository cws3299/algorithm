import sys
sys.stdin = open('17835.txt','r')
import heapq

def dijkstra():
    global n,m,k,roads,companys

    answer = [float('inf')]*(n+1)
    pq = []
    for company in companys:
        # print('company',company)
        heapq.heappush(pq,[0,company])
        answer[company] = 0

    while pq:
        now_distance, now_position = heapq.heappop(pq)

        if answer[now_position] < now_distance:
            continue

        for nxt,wt in roads[now_position].items():
            distance = now_distance + wt
            if answer[nxt] > distance:
                answer[nxt] = distance
                heapq.heappush(pq,[distance,nxt])
    
    return answer

n,m,k = map(int, input().split())
roads = {node:{} for node in range(n+1)}

for _ in range(m):
    s,e,w = map(int, input().split())
    value = roads.get(e)
    vv = value.get(s)
    if vv == None or vv > w:
        roads[e][s] = w
# print(roads)

companys = list(map(int, input().split()))

ans = dijkstra()
ans = ans[1:]

_max = max(ans)
index = ans.index(_max)
print(index+1)
print(_max)

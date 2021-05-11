import sys
sys.stdin = open('14554.txt','r')
import heapq

def dijkstra():
    global n,m,s,e,arr,answers

    answer= [[float('inf'),0] for _ in range(n+1)]
    pq = []
    answer[s][0] = 0
    heapq.heappush(pq,[answer[s][0],s,1])
    first_distance = None

    while pq:
        now_distance , now_positon, numbers = heapq.heappop(pq)

        if first_distance != None and now_distance > first_distance:
            break

        if now_positon == e:
            first_distance = now_distance
            answer[now_positon][1] += numbers

        if answer[now_positon][0] < now_distance:
            continue

        for nxt_route in arr[now_positon].keys():
            wt = arr[now_positon][nxt_route][0]
            number = arr[now_positon][nxt_route][1]
            if number > 0:
                distance = now_distance+wt
                if answer[nxt_route][0] >= distance:
                    answer[nxt_route][0] = distance
                    heapq.heappush(pq,[answer[nxt_route][0],nxt_route,numbers*number])

    answers = answer[e][1] % ((10**9)+9)
    return

n,m,s,e = map(int, input().split())
arr = {node:{} for node in range(n+1)}

for _ in range(m):
    a,b,w = map(int, input().split())
    value = arr.get(a)
    vv= value.get(b)
    if vv == None:
        arr[a][b] = [w,1]
        arr[b][a] = [w,1]
    # print(arr[a][b])
    elif arr[a][b][0] == w:
        arr[a][b][1] += 1
        arr[b][a][1] += 1
    elif arr[a][b][0] > w:
        arr[a][b][0] = w
        arr[a][b][1] = 1

answers = False
dijkstra()
print(answers)


import sys
sys.stdin = open('5214.txt','r')
from collections import deque

def bfs():
    global n,c,k,stations,tubes,visit_stations,visit_tubes

    q = deque()
    visit_stations[1] = 1
    q.append([1,1])

    while q:
        now_station,number = q.popleft()

        if now_station == n:
            return number

        for nxt_tube in stations[now_station]:
            if visit_tubes[nxt_tube] == 0:
                visit_tubes[nxt_tube] = 1
                for nxt_station in tubes[nxt_tube]:
                    if visit_stations[nxt_station] == 0:
                        visit_stations[nxt_station] = 1
                        q.append([nxt_station,number+1])

    return False

n,c,k = map(int, input().split())
stations = [[] for _ in range(n+1)]
tubes = [[]]

for s in range(1,k+1):
    tube = list(map(int, input().split()))
    tubes.append(tube)
    for tu in tube:
        stations[tu].append(s)

visit_stations = [0]*(n+1)
visit_tubes = [0]*(k+1)

print(stations)
print(tubes)
print(visit_stations)
print(visit_tubes)

answer = bfs()

if answer == False:
    print(-1)
else:
    print(answer)

import sys
sys.stdin = open('1379.txt','r')
import heapq

n = int(input())
pq = []

for _ in range(n):
    c,s,e = map(int, input().split())
    heapq.heappush(pq,[s,e,c])

tq = []
rooms = [-1] + [0]*(n)
answer = 0
answer_lst = [-1]*(n+1)


while pq:
    start,end,cla = heapq.heappop(pq)

    while tq and tq[0][0] <= start:
        ed , cl , ss = heapq.heappop(tq)
        rooms[ss] = 0

    sss = rooms.index(0)

    if sss > answer:
        answer = sss

    rooms[sss] = 1
    # print(start,end,cla,sss)
    answer_lst[cla] = sss

    heapq.heappush(tq,[end,cla,sss])

# print(answer_lst)
# print(answer)

# print('-------------------------------------------')
# print(answer_lst)
print(answer)
for ans in answer_lst[1:]:
    print(ans)